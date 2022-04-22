-- Deploy eurus-backend-db-report:20211220_alter_report_audit_generate to pg

BEGIN;
DROP FUNCTION public.report_audit_generate;

CREATE OR REPLACE FUNCTION public.report_audit_generate(var_selected_date date)
 RETURNS TABLE(asset_name character varying, total_supply numeric, previous_total_supply numeric, total_supply_change numeric, mainnet_cold_wallet_current_balance numeric, mainnet_cold_wallet_previous_balance numeric, mainnet_hot_wallet_current_balance numeric, mainnet_hot_wallet_previous_balance numeric, mainnet_hot_balance_change numeric, mainnet_cold_balance_change numeric, side_chain_to_mainnet_admin_fee numeric, side_chain_to_mainnet_count integer, side_chain_to_mainnet_sum numeric, mainnet_to_side_chain_count integer, mainnet_to_side_chain_sum numeric, side_chain_to_side_chain_count integer, side_chain_to_side_chain_sum numeric, selected_date date, created_date timestamp with time zone, last_modified_date timestamp with time zone)
 LANGUAGE plpgsql
AS $function$
begin
	
	RAISE NOTICE 'Starts report_audit_generate at : %, selected date: % ', now(), var_selected_date; 
	-- 1. Insert all used asset name to [report_audit]
	perform report_audit_insert_asset(var_selected_date);
    -- 2. Calculate balance change
	perform report_audit_cal_bal_change_upsert(var_selected_date);
    -- 3. Calculate deposit amount lump sum, number of transactions of [var_selected_date] (Main->Side)
	perform report_audit_cal_deposit_transactions_upsert(var_selected_date);
    -- 4. Calculate withdraw amount lump sum, admin fee lump sum, number of transactions of [var_selected_date] (Side->Main)
	perform report_audit_cal_withdraw_transactions_upsert(var_selected_date);
	-- 5. Calculate transfer amount lump sum, number of transactions of [var_selected_date] (Side->Side)
	perform report_audit_cal_transfer_transactions_upsert(var_selected_date,2021);
	RAISE NOTICE 'End report_audit_generate at :%, selected date : % ', now(), var_selected_date; 
	
    return query 
    select ra.asset_name ,  
    ats.total_supply / power(10, a."decimal")::numeric(78, 18) as total_supply,
    ats1.total_supply / power(10, a."decimal")::numeric(78, 18) as previous_total_supply,
    (coalesce(ats.total_supply, 0) - coalesce(ats1.total_supply, 0))::numeric(78, 18)  / power(10, a."decimal")::numeric(78, 18)  as total_supply_change,
	(ra.mainnet_cold_wallet_current_balance  / power(10, a."decimal" ))::numeric(78, 18) as mainnet_cold_wallet_current_balance,
	(ra.mainnet_cold_wallet_previous_balance / power(10,  a."decimal"))::numeric(78, 18) as mainnet_cold_wallet_previous_balance,
	(ra.mainnet_hot_wallet_current_balance  / power(10, a."decimal" ))::numeric(78, 18) as mainnet_hot_wallet_current_balance,
	(ra.mainnet_hot_wallet_previous_balance / power(10,  a."decimal"))::numeric(78, 18) as mainnet_hot_wallet_previous_balance,
	(ra.mainnet_hot_balance_change  / power(10, a."decimal" ))::numeric(78, 18) as mainnet_hot_balance_change,
	(ra.mainnet_cold_balance_change / power(10,  a."decimal"))::numeric(78, 18) as mainnet_cold_balance_change,
	(ra.side_chain_to_mainnet_admin_fee  / power(10, a."decimal"))::numeric(78, 18)as side_chain_to_mainnet_admin_fee,
	ra.side_chain_to_mainnet_count ,
	(ra.side_chain_to_mainnet_sum  /  power(10,  a."decimal"))::numeric(78, 18) as side_chain_to_mainnet_sum,
	ra.mainnet_to_side_chain_count ,
	(ra.mainnet_to_side_chain_sum  / power(10,  a."decimal"))::numeric(78, 18) as mainnet_to_side_chain_sum,
	ra.side_chain_to_side_chain_count ,
	(ra.side_chain_to_side_chain_sum  / power(10,  a."decimal"))::numeric(78, 18) as side_chain_to_side_chain_sum,
	var_selected_date as selected_date,
	ra.created_date,
	ra.last_modified_date
	from report_audit ra 
	inner join assets as a on a.asset_name = ra.asset_name 
	left join asset_total_supplies ats  on ats.asset_name = a.asset_name and date(ats.mark_date)  = ra.selected_date
	left join asset_total_supplies ats1 on ats1.asset_name = a.asset_name and date(ats1.mark_date)  = ra.selected_date::date - 1
	where ra.selected_date = var_selected_date
	order by ra.asset_name;
end;

$function$
;


COMMIT;
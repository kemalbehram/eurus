-- Verify eurus-backend-db-report:2021_08_18_report_audit_cal_bal_change_upsert on pg

BEGIN;

-- XXX Add verifications here.
select report_audit_cal_bal_change_upsert('2021-08-15');

ROLLBACK;

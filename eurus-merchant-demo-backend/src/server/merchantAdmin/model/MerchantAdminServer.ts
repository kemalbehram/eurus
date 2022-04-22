import winston from 'winston';
import { ServerBase } from '../../../foundation/server/ServerBase';
import { DepositObserver } from '../observer/DepositObserver';
import { WithdrawObserver } from '../observer/WithdrawObserver';
import logger from '../util/ServiceLogger';

export class MerchantAdminServer extends ServerBase {
  depositObserver?: DepositObserver;
  withdrawObserver?: WithdrawObserver;
  logger?: winston.Logger; // you can import this logger by import or just use MerchantAdminServer.logger by instance
  constructor() {
    super();
    this.logger = logger;
  }
}

let deployHelper = require('./deploy_helper');

var pla = artifacts.require("EurusERC20");
var ownedProxy = artifacts.require("OwnedUpgradeabilityProxy");
var internalSCConfig = artifacts.require("InternalSmartContractConfig");

const erc20Json = require("./../build/contracts/EurusERC20.json");
const externalSCConfigJson = require("./../build/contracts/ExternalSmartContractConfig.json");

module.exports = async function (deployer) {
    deployHelper.readDeployLog();

    let ownedProxyInstance;

    await deployHelper.deployWithProxy(deployer, pla, 'PLA', ownedProxy)

    await pla.deployed();
    ownedProxyInstance = await ownedProxy.deployed();

    // let accounts = await web3.eth.getAccounts();
    // let bnbobj = new web3.eth.Contract(erc20Json.abi, ownedProxyInstance.address);
    // let err= await bnbobj.methods.init(internalSCConfig.address, "BAL", "BAL", 114690000000000000000000000n, 18).send(await deployHelper.callParams(accounts));
    // console.log("init function tx receipt: " + JSON.stringify(err));

    // console.log("Register BAL to ExternalSmartContractConfig" );
    // let extSCInfo = deployHelper.getSmartContractInfoByName(deployer, 'ExternalSmartContractConfig');
    // let externalScObj = new web3.eth.Contract(externalSCConfigJson.abi,extSCInfo.address)

    // await externalScObj.methods.removeCurrencyInfo("BAL").send(await deployHelper.callParams(accounts));
    // await externalScObj.methods.addCurrencyInfo(ownedProxyInstance.address, "BAL").send(await deployHelper.callParams(accounts));

    deployHelper.writeDeployLog();
};
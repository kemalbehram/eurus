let deployHelper = require('./deploy_helper');

var zil = artifacts.require("EurusERC20");

const erc20Json = require("./../build/contracts/EurusERC20.json");
const ownedProxyJson = require("./../build/contracts/OwnedUpgradeabilityProxy.json");
module.exports = async function (deployer) {
    deployHelper.readDeployLog();

    await deployHelper.deploy(deployer,zil,"ZIL")
    let zilInstance = await zil.deployed();
    let accounts = await web3.eth.getAccounts();


    let ownedProxyObj = deployHelper.getSmartContractInfoByName(deployer, "OwnedUpgradeabilityProxy<ZIL>");
    let ownedProxyInstance = new web3.eth.Contract(ownedProxyJson.abi,ownedProxyObj.address);
    await ownedProxyInstance.methods.upgradeTo(zilInstance.address).send(await deployHelper.callParams(accounts, deployer));



    // let blacklistSC = deployHelper.getSmartContractInfoByName(deployer, "OwnedUpgradeabilityProxy<ZIL>");
    // let blacklistSCObj = new web3.eth.Contract(erc20Json.abi,blacklistSC.address)
    //
    // let EurusUserDeposit = deployHelper.getSmartContractInfoByName(deployer, "OwnedUpgradeabilityProxy<EurusUserDeposit>");
    //
    // await blacklistSCObj.methods.addBlackListDestAddress(EurusUserDeposit.address).send(await deployHelper.callParams(accounts));

    deployHelper.writeDeployLog();
};
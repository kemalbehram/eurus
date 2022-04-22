let deployHelper = require('./deploy_helper');

var uni = artifacts.require("EurusERC20");
var ownedProxy = artifacts.require("OwnedUpgradeabilityProxy");
var internalSCConfig = artifacts.require("InternalSmartContractConfig");

const erc20Json = require("./../build/contracts/EurusERC20.json");
const externalSCConfigJson = require("./../build/contracts/ExternalSmartContractConfig.json");

module.exports = async function (deployer) {
    deployHelper.readDeployLog();

    let ownedProxyInstance;

    await deployHelper.deployWithProxy(deployer, uni, 'UNI', ownedProxy)

    await uni.deployed();
    ownedProxyInstance = await ownedProxy.deployed();

    // let accounts = await web3.eth.getAccounts();
    // let uniobj = new web3.eth.Contract(erc20Json.abi, ownedProxyInstance.address);
    // let err= await uniobj.methods.init(internalSCConfig.address, "UNI", "UNI", 13242013521397079n, 18).send(await deployHelper.callParams(accounts, deployer));
    // console.log("init function tx receipt: " + JSON.stringify(err));

    // console.log("Register UNI to ExternalSmartContractConfig" );
    // let extSCInfo = deployHelper.getSmartContractInfoByName(deployer, 'ExternalSmartContractConfig');
    // let externalScObj = new web3.eth.Contract(externalSCConfigJson.abi,extSCInfo.address)

    // await externalScObj.methods.removeCurrencyInfo("UNI").send(await deployHelper.callParams(accounts, deployer));
    // await externalScObj.methods.addCurrencyInfo(ownedProxyInstance.address, "UNI").send(await deployHelper.callParams(accounts, deployer));

    deployHelper.writeDeployLog();
};
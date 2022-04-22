const fs = require('fs');
let smartContractMap = {};

module.exports.smartContractMap = smartContractMap;

module.exports.rinkebyCallParams=async(accounts)=>{
    return new Promise(async(res,rej)=>{
        return res({
            from: accounts[0],
            gasLimit: 10000000,
            gasPrice: 128000000000
        });
    })

}

module.exports.callParams = async (accounts)=>{
    return new Promise(async(res,rej)=>{
        return res({
            from: accounts[0],
            gas: 100000000,
            gasPrice: 137500000
        });
    })

}

module.exports.localCallParams = async(accounts)=>{
    return new Promise(async(res,rej)=>{
        return res({
            from: accounts[0],
            gasLimit: 6721975,
            gasPrice: 1000000,
            gas: 6721975
        });
    })

}

module.exports.deployWithProxy = async function(deployer, contract, contractNameOrNull, proxyContract){
    return new Promise(async(res,rej)=>{

        ! (deployer.network_id in this.smartContractMap) && (this.smartContractMap[deployer.network_id] = {'smartContract':{}});

        let deployedContract = await deployer.deploy(contract);

        let contractName = (contractNameOrNull == null)? contract.contractName:contractNameOrNull;

        let contractInstance = await contract.deployed();
        this.smartContractMap[deployer.network_id]['smartContract'][contractName] = { address: contractInstance.address};

        let deployedProxy = await deployer.deploy(proxyContract);
        let proxyInstance = await proxyContract.deployed();
        let proxyContractName = proxyContract.contractName + "<" + contractName + ">";
        this.smartContractMap[deployer.network_id]['smartContract'][proxyContractName] = {address: proxyInstance.address};

        console.log(contractName + ' ' + contractInstance.address);
        console.log(proxyContractName + ' ' + proxyInstance.address);
        await proxyInstance.upgradeTo(contractInstance.address);


        return res(0);
    })


}

module.exports.deployWithProxyWithFixedProxyContractName = async function(deployer, contract, proxyContract, proxyContractName) {
    return new Promise(async (res, rej) => {
        !(deployer.network_id in this.smartContractMap) && (this.smartContractMap[deployer.network_id] = {'smartContract':{}});

        let deployedContract = await deployer.deploy(contract);
        let contractInstance = await contract.deployed();
        this.smartContractMap[deployer.network_id]['smartContract'][contract.contractName] = { address: contractInstance.address};

        let deployedProxy = await deployer.deploy(proxyContract);
        let proxyInstance = await proxyContract.deployed();
        this.smartContractMap[deployer.network_id]['smartContract'][proxyContractName] = {address: proxyInstance.address};

        console.log(contract.contractName + ' ' + contractInstance.address);
        console.log(proxyContractName + ' ' + proxyInstance.address);
        await proxyInstance.upgradeTo(contract.address);

        return res(0);
    });
}

module.exports.deploy = async function(deployer, contract, ...args){
    return new Promise(async(res,rej)=>{
        ! (deployer.network_id in this.smartContractMap) && (this.smartContractMap[deployer.network_id] = {'smartContract':{}});


        await deployer.deploy(contract, ...args);
        let instance = await contract.deployed();
        console.log(contract.contractName + ' ' + instance.address);
        this.smartContractMap[deployer.network_id]['smartContract'][contract.contractName] = { address: instance.address};
        return res(0);
    })
}




module.exports.getSmartContractInfoByName = function(deployer, contractName){
    return this.smartContractMap[deployer.network_id]["smartContract"][contractName];
}

let deployFileName;
module.exports.readDeployLog = function() {
    
    try{
        let suffix = config.network;
        let index = suffix.indexOf('_');
        if (index >= 0){
            suffix = suffix.substring(0, index);
        }
        deployFileName = 'SmartContractDeploy_' + suffix + '.json';

        var rawData = fs.readFileSync('../smartcontract/SmartContractDeploy_' + suffix + '.json');
        if (rawData.length > 0) {
            this.smartContractMap = JSON.parse(rawData);
        }
    }catch (ex) {
        console.log("readDeployLog: " + ex);
    }
}

module.exports.writeDeployLog = function(){

    this.smartContractMap.lastUpdateTime = new Date().toISOString();
    let jsonStr = JSON.stringify(this.smartContractMap);

    if (deployFileName && deployFileName != '' ){
        fs.writeFileSync('../smartcontract/'+deployFileName, jsonStr);
    }else {
        console.log('deployFileName is not defined, cannot write to file');
    }
}

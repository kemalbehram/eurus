multicall_v2_abi = [
    {
        "inputs": [
            {
                "components": [
                    {"internalType": "address", "name": "target", "type": "address"},
                    {"internalType": "bytes", "name": "callData", "type": "bytes"},
                ],
                "internalType": "struct Multicall2.Call[]",
                "name": "calls",
                "type": "tuple[]",
            }
        ],
        "name": "aggregate",
        "outputs": [
            {"internalType": "uint256", "name": "blockNumber", "type": "uint256"},
            {"internalType": "bytes[]", "name": "returnData", "type": "bytes[]"},
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {"internalType": "address", "name": "target", "type": "address"},
                    {"internalType": "bytes", "name": "callData", "type": "bytes"},
                ],
                "internalType": "struct Multicall2.Call[]",
                "name": "calls",
                "type": "tuple[]",
            }
        ],
        "name": "blockAndAggregate",
        "outputs": [
            {"internalType": "uint256", "name": "blockNumber", "type": "uint256"},
            {"internalType": "bytes32", "name": "blockHash", "type": "bytes32"},
            {
                "components": [
                    {"internalType": "bool", "name": "success", "type": "bool"},
                    {"internalType": "bytes", "name": "returnData", "type": "bytes"},
                ],
                "internalType": "struct Multicall2.Result[]",
                "name": "returnData",
                "type": "tuple[]",
            },
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "blockNumber", "type": "uint256"}
        ],
        "name": "getBlockHash",
        "outputs": [
            {"internalType": "bytes32", "name": "blockHash", "type": "bytes32"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getBlockNumber",
        "outputs": [
            {"internalType": "uint256", "name": "blockNumber", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getCurrentBlockCoinbase",
        "outputs": [{"internalType": "address", "name": "coinbase", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getCurrentBlockDifficulty",
        "outputs": [
            {"internalType": "uint256", "name": "difficulty", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getCurrentBlockGasLimit",
        "outputs": [{"internalType": "uint256", "name": "gaslimit", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getCurrentBlockTimestamp",
        "outputs": [
            {"internalType": "uint256", "name": "timestamp", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "addr", "type": "address"}],
        "name": "getEthBalance",
        "outputs": [{"internalType": "uint256", "name": "balance", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getLastBlockHash",
        "outputs": [
            {"internalType": "bytes32", "name": "blockHash", "type": "bytes32"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bool", "name": "requireSuccess", "type": "bool"},
            {
                "components": [
                    {"internalType": "address", "name": "target", "type": "address"},
                    {"internalType": "bytes", "name": "callData", "type": "bytes"},
                ],
                "internalType": "struct Multicall2.Call[]",
                "name": "calls",
                "type": "tuple[]",
            },
        ],
        "name": "tryAggregate",
        "outputs": [
            {
                "components": [
                    {"internalType": "bool", "name": "success", "type": "bool"},
                    {"internalType": "bytes", "name": "returnData", "type": "bytes"},
                ],
                "internalType": "struct Multicall2.Result[]",
                "name": "returnData",
                "type": "tuple[]",
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bool", "name": "requireSuccess", "type": "bool"},
            {
                "components": [
                    {"internalType": "address", "name": "target", "type": "address"},
                    {"internalType": "bytes", "name": "callData", "type": "bytes"},
                ],
                "internalType": "struct Multicall2.Call[]",
                "name": "calls",
                "type": "tuple[]",
            },
        ],
        "name": "tryBlockAndAggregate",
        "outputs": [
            {"internalType": "uint256", "name": "blockNumber", "type": "uint256"},
            {"internalType": "bytes32", "name": "blockHash", "type": "bytes32"},
            {
                "components": [
                    {"internalType": "bool", "name": "success", "type": "bool"},
                    {"internalType": "bytes", "name": "returnData", "type": "bytes"},
                ],
                "internalType": "struct Multicall2.Result[]",
                "name": "returnData",
                "type": "tuple[]",
            },
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

multicall_v2_bytecode = b'`\x80`@R4\x80\x15a\x00\x10W`\x00\x80\xfd[Pa\t\xd3\x80a\x00 `\x009`\x00\xf3\xfe`\x80`@R4\x80\x15a\x00\x10W`\x00\x80\xfd[P`\x046\x10a\x00\xb4W`\x005`\xe0\x1c\x80crB]\x9d\x11a\x00qW\x80crB]\x9d\x14a\x01:W\x80c\x86\xd5\x16\xe8\x14a\x01@W\x80c\xa8\xb0WN\x14a\x01FW\x80c\xbc\xe3\x8b\xd7\x14a\x01TW\x80c\xc3\x07\x7f\xa9\x14a\x01tW\x80c\xee\x82\xac^\x14a\x01\x87Wa\x00\xb4V[\x80c\x0f(\xc9}\x14a\x00\xb9W\x80c%-\xbaB\x14a\x00\xceW\x80c\'\xe8mn\x14a\x00\xefW\x80c9\x95B\xe9\x14a\x00\xf7W\x80cB\xcb\xb1\\\x14a\x01\x19W\x80cM#\x01\xcc\x14a\x01\x1fW[`\x00\x80\xfd[B[`@Q\x90\x81R` \x01[`@Q\x80\x91\x03\x90\xf3[a\x00\xe1a\x00\xdc6`\x04a\x06\xe2V[a\x01\x99V[`@Qa\x00\xc5\x92\x91\x90a\x08NV[a\x00\xbba\x03YV[a\x01\na\x01\x056`\x04a\x07\x1dV[a\x03lV[`@Qa\x00\xc5\x93\x92\x91\x90a\x08\xb6V[Ca\x00\xbbV[a\x00\xbba\x01-6`\x04a\x06\xc1V[`\x01`\x01`\xa0\x1b\x03\x161\x90V[Da\x00\xbbV[Ea\x00\xbbV[`@QA\x81R` \x01a\x00\xc5V[a\x01ga\x01b6`\x04a\x07\x1dV[a\x03\x84V[`@Qa\x00\xc5\x91\x90a\x08;V[a\x01\na\x01\x826`\x04a\x06\xe2V[a\x05vV[a\x00\xbba\x01\x956`\x04a\x07oV[@\x90V[\x80QC\x90``\x90g\xff\xff\xff\xff\xff\xff\xff\xff\x81\x11\x15a\x01\xc6WcNH{q`\xe0\x1b`\x00R`A`\x04R`$`\x00\xfd[`@Q\x90\x80\x82R\x80` \x02` \x01\x82\x01`@R\x80\x15a\x01\xf9W\x81` \x01[``\x81R` \x01\x90`\x01\x90\x03\x90\x81a\x01\xe4W\x90P[P\x90P`\x00[\x83Q\x81\x10\x15a\x03SW`\x00\x80\x85\x83\x81Q\x81\x10a\x02+WcNH{q`\xe0\x1b`\x00R`2`\x04R`$`\x00\xfd[` \x02` \x01\x01Q`\x00\x01Q`\x01`\x01`\xa0\x1b\x03\x16\x86\x84\x81Q\x81\x10a\x02`WcNH{q`\xe0\x1b`\x00R`2`\x04R`$`\x00\xfd[` \x02` \x01\x01Q` \x01Q`@Qa\x02y\x91\x90a\x08\x1fV[`\x00`@Q\x80\x83\x03\x81`\x00\x86Z\xf1\x91PP=\x80`\x00\x81\x14a\x02\xb6W`@Q\x91P`\x1f\x19`?=\x01\x16\x82\x01`@R=\x82R=`\x00` \x84\x01>a\x02\xbbV[``\x91P[P\x91P\x91P\x81a\x03\x12W`@QbF\x1b\xcd`\xe5\x1b\x81R` `\x04\x82\x01\x81\x90R`$\x82\x01R\x7fMulticall aggregate: call failed`D\x82\x01R`d\x01[`@Q\x80\x91\x03\x90\xfd[\x80\x84\x84\x81Q\x81\x10a\x033WcNH{q`\xe0\x1b`\x00R`2`\x04R`$`\x00\xfd[` \x02` \x01\x01\x81\x90RPPP\x80\x80a\x03K\x90a\tVV[\x91PPa\x01\xffV[P\x91P\x91V[`\x00a\x03f`\x01Ca\t\x0fV[@\x90P\x90V[C\x80@``a\x03{\x85\x85a\x03\x84V[\x90P\x92P\x92P\x92V[``\x81Qg\xff\xff\xff\xff\xff\xff\xff\xff\x81\x11\x15a\x03\xaeWcNH{q`\xe0\x1b`\x00R`A`\x04R`$`\x00\xfd[`@Q\x90\x80\x82R\x80` \x02` \x01\x82\x01`@R\x80\x15a\x03\xf4W\x81` \x01[`@\x80Q\x80\x82\x01\x90\x91R`\x00\x81R``` \x82\x01R\x81R` \x01\x90`\x01\x90\x03\x90\x81a\x03\xccW\x90P[P\x90P`\x00[\x82Q\x81\x10\x15a\x05oW`\x00\x80\x84\x83\x81Q\x81\x10a\x04&WcNH{q`\xe0\x1b`\x00R`2`\x04R`$`\x00\xfd[` \x02` \x01\x01Q`\x00\x01Q`\x01`\x01`\xa0\x1b\x03\x16\x85\x84\x81Q\x81\x10a\x04[WcNH{q`\xe0\x1b`\x00R`2`\x04R`$`\x00\xfd[` \x02` \x01\x01Q` \x01Q`@Qa\x04t\x91\x90a\x08\x1fV[`\x00`@Q\x80\x83\x03\x81`\x00\x86Z\xf1\x91PP=\x80`\x00\x81\x14a\x04\xb1W`@Q\x91P`\x1f\x19`?=\x01\x16\x82\x01`@R=\x82R=`\x00` \x84\x01>a\x04\xb6V[``\x91P[P\x91P\x91P\x85\x15a\x05\x18W\x81a\x05\x18W`@QbF\x1b\xcd`\xe5\x1b\x81R` `\x04\x82\x01R`!`$\x82\x01R\x7fMulticall2 aggregate: call faile`D\x82\x01R`\x19`\xfa\x1b`d\x82\x01R`\x84\x01a\x03\tV[`@Q\x80`@\x01`@R\x80\x83\x15\x15\x81R` \x01\x82\x81RP\x84\x84\x81Q\x81\x10a\x05OWcNH{q`\xe0\x1b`\x00R`2`\x04R`$`\x00\xfd[` \x02` \x01\x01\x81\x90RPPP\x80\x80a\x05g\x90a\tVV[\x91PPa\x03\xfaV[P\x92\x91PPV[`\x00\x80``a\x05\x86`\x01\x85a\x03lV[\x91\x96\x90\x95P\x90\x93P\x91PPV[\x805`\x01`\x01`\xa0\x1b\x03\x81\x16\x81\x14a\x05\xaaW`\x00\x80\xfd[\x91\x90PV[`\x00\x82`\x1f\x83\x01\x12a\x05\xbfW\x80\x81\xfd[\x815` g\xff\xff\xff\xff\xff\xff\xff\xff\x80\x83\x11\x15a\x05\xdcWa\x05\xdca\t\x87V[a\x05\xe9\x82\x83\x85\x02\x01a\x08\xdeV[\x83\x81R\x82\x81\x01\x90\x86\x84\x01\x86[\x86\x81\x10\x15a\x06\xb3W\x815\x89\x01`@`\x1f\x19\x81\x81\x84\x8f\x03\x01\x12\x15a\x06\x16W\x8a\x8b\xfd[a\x06\x1f\x82a\x08\xdeV[a\x06*\x8a\x85\x01a\x05\x93V[\x81R\x82\x84\x015\x89\x81\x11\x15a\x06<W\x8c\x8d\xfd[\x80\x85\x01\x94PP\x8d`?\x85\x01\x12a\x06PW\x8b\x8c\xfd[\x89\x84\x015\x89\x81\x11\x15a\x06dWa\x06da\t\x87V[a\x06t\x8b\x84`\x1f\x84\x01\x16\x01a\x08\xdeV[\x92P\x80\x83R\x8e\x84\x82\x87\x01\x01\x11\x15a\x06\x89W\x8c\x8d\xfd[\x80\x84\x86\x01\x8c\x85\x017\x82\x01\x8a\x01\x8c\x90R\x80\x8a\x01\x91\x90\x91R\x86RPP\x92\x85\x01\x92\x90\x85\x01\x90`\x01\x01a\x05\xf5V[P\x90\x98\x97PPPPPPPPV[`\x00` \x82\x84\x03\x12\x15a\x06\xd2W\x80\x81\xfd[a\x06\xdb\x82a\x05\x93V[\x93\x92PPPV[`\x00` \x82\x84\x03\x12\x15a\x06\xf3W\x80\x81\xfd[\x815g\xff\xff\xff\xff\xff\xff\xff\xff\x81\x11\x15a\x07\tW\x81\x82\xfd[a\x07\x15\x84\x82\x85\x01a\x05\xafV[\x94\x93PPPPV[`\x00\x80`@\x83\x85\x03\x12\x15a\x07/W\x80\x81\xfd[\x825\x80\x15\x15\x81\x14a\x07>W\x81\x82\xfd[\x91P` \x83\x015g\xff\xff\xff\xff\xff\xff\xff\xff\x81\x11\x15a\x07YW\x81\x82\xfd[a\x07e\x85\x82\x86\x01a\x05\xafV[\x91PP\x92P\x92\x90PV[`\x00` \x82\x84\x03\x12\x15a\x07\x80W\x80\x81\xfd[P5\x91\x90PV[`\x00\x82\x82Q\x80\x85R` \x80\x86\x01\x95P\x80\x81\x83\x02\x84\x01\x01\x81\x86\x01\x85[\x84\x81\x10\x15a\x07\xe6W\x85\x83\x03`\x1f\x19\x01\x89R\x81Q\x80Q\x15\x15\x84R\x84\x01Q`@\x85\x85\x01\x81\x90Ra\x07\xd2\x81\x86\x01\x83a\x07\xf3V[\x9a\x86\x01\x9a\x94PPP\x90\x83\x01\x90`\x01\x01a\x07\xa2V[P\x90\x97\x96PPPPPPPV[`\x00\x81Q\x80\x84Ra\x08\x0b\x81` \x86\x01` \x86\x01a\t&V[`\x1f\x01`\x1f\x19\x16\x92\x90\x92\x01` \x01\x92\x91PPV[`\x00\x82Qa\x081\x81\x84` \x87\x01a\t&V[\x91\x90\x91\x01\x92\x91PPV[`\x00` \x82Ra\x06\xdb` \x83\x01\x84a\x07\x87V[`\x00`@\x82\x01\x84\x83R` `@\x81\x85\x01R\x81\x85Q\x80\x84R``\x86\x01\x91P``\x83\x82\x02\x87\x01\x01\x93P\x82\x87\x01\x85[\x82\x81\x10\x15a\x08\xa8W`_\x19\x88\x87\x03\x01\x84Ra\x08\x96\x86\x83Qa\x07\xf3V[\x95P\x92\x84\x01\x92\x90\x84\x01\x90`\x01\x01a\x08zV[P\x93\x98\x97PPPPPPPPV[`\x00\x84\x82R\x83` \x83\x01R```@\x83\x01Ra\x08\xd5``\x83\x01\x84a\x07\x87V[\x95\x94PPPPPV[`@Q`\x1f\x82\x01`\x1f\x19\x16\x81\x01g\xff\xff\xff\xff\xff\xff\xff\xff\x81\x11\x82\x82\x10\x17\x15a\t\x07Wa\t\x07a\t\x87V[`@R\x91\x90PV[`\x00\x82\x82\x10\x15a\t!Wa\t!a\tqV[P\x03\x90V[`\x00[\x83\x81\x10\x15a\tAW\x81\x81\x01Q\x83\x82\x01R` \x01a\t)V[\x83\x81\x11\x15a\tPW`\x00\x84\x84\x01R[PPPPV[`\x00`\x00\x19\x82\x14\x15a\tjWa\tja\tqV[P`\x01\x01\x90V[cNH{q`\xe0\x1b`\x00R`\x11`\x04R`$`\x00\xfd[cNH{q`\xe0\x1b`\x00R`A`\x04R`$`\x00\xfd\xfe\xa2dipfsX"\x12 g\x87\xfa\xa4\xe9\x95"\xd9\x928\xbf\xcc\xae}\xb6c@m_\xb7m2\xf8S\x95\xe2\x07m73\xa7\xcddsolcC\x00\x08\x02\x003'

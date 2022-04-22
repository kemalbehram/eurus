import { ChainId } from 'moonbeamswapdada'
import MULTICALL_ABI from './abi.json'
import { multicall } from '../../moonbase_address.json'

const MULTICALL_NETWORKS: { [chainId in ChainId]: string } = {
  [ChainId.MAINNET]: '0xeefBa1e63905eF1D7ACbA5a8513c70307C1cE441',
  [ChainId.STANDALONE]: '0xF8cef78E923919054037a1D03662bBD884fF4edf',
  [ChainId.MOONROCK]: multicall,
  [ChainId.MOONBASE]: multicall,
  [ChainId.BESUDEV]: '0x68E28a3acc6586Dab64E78dBb1DdE959411F6819',
  [ChainId.MOONSHADOW]: multicall
}

export { MULTICALL_ABI, MULTICALL_NETWORKS }

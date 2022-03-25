import csv

opcodes_dic = {
    'STOP' :1,
    'ADD' :1,
    'MUL' :1,
    'SUB' :1,
    'DIV' :1,
    'SDIV' :1,
    'MOD' :1,
    'SMOD' :1,
    'ADDMOD' :1,
    'MULMOD' :1,
    'EXP' :1,
    'SIGNEXTEND' :1,
    'LT' :1,
    'GT' :1,
    'SLT' :1,
    'SGT' :1,
    'EQ' :1,
    'ISZERO' :1,
    'AND' :1,
    'OR' :1,
    'XOR' :1,
    'NOT' :1,
    'BYTE' :1,
    'SHL' :1,
    'SHR' :1,
    'SAR' :1,
    'SHA3' :1,
    'ADDRESS' :1,
    'BALANCE' :1,
    'ORIGIN' :1,
    'CALLER' :1,
    'CALLVALUE' :1,
    'CALLDATALOAD' :1,
    'CALLDATASIZE' :1,
    'CALLDATACOPY' :1,
    'CODESIZE' :1,
    'CODECOPY' :1,
    'GASPRICE' :1,
    'EXTCODESIZE' :1,
    'EXTCODECOPY' :1,
    'RETURNDATASIZE' :1,
    'RETURNDATACOPY' :1,
    'EXTCODEHASH' :1,
    'BLOCKHASH' :1,
    'COINBASE' :1,
    'TIMESTAMP' :1,
    'NUMBER' :1,
    'DIFFICULTY' :1,
    'GASLIMIT' :1,
    'POP' :1,
    'MLOAD' :1,
    'MSTORE' :1,
    'MSTORE8' :1,
    'SLOAD' :1,
    'SSTORE' :1,
    'JUMP' :1,
    'JUMPI' :1,
    'PC' :1,
    'MSIZE' :1,
    'GAS' :1,
    'JUMPDEST' :1,
    'PUSH1' :2,
    'PUSH2' :2,
    'PUSH3' :2,
    'PUSH4' :2,
    'PUSH5' :2,
    'PUSH6' :2,
    'PUSH7' :2,
    'PUSH8' :2,
    'PUSH9' :2,
    'PUSH10' :2,
    'PUSH11' :2,
    'PUSH12' :2,
    'PUSH13' :2,
    'PUSH14' :2,
    'PUSH15' :2,
    'PUSH16' :2,
    'PUSH17' :2,
    'PUSH18' :2,
    'PUSH19' :2,
    'PUSH20' :2,
    'PUSH21' :2,
    'PUSH22' :2,
    'PUSH23' :2,
    'PUSH24' :2,
    'PUSH25' :2,
    'PUSH26' :2,
    'PUSH27' :2,
    'PUSH28' :2,
    'PUSH29' :2,
    'PUSH30' :2,
    'PUSH31' :2,
    'PUSH32' :2,
    'DUP1' :2,
    'DUP2' :2,
    'DUP3' :2,
    'DUP4' :2,
    'DUP5' :2,
    'DUP6' :2,
    'DUP7' :2,
    'DUP8' :2,
    'DUP9' :2,
    'DUP10' :2,
    'DUP11' :2,
    'DUP12' :2,
    'DUP13' :2,
    'DUP14' :2,
    'DUP15' :2,
    'DUP16' :2,
    'SWAP1' :2,
    'SWAP2' :2,
    'SWAP3' :2,
    'SWAP4' :2,
    'SWAP5' :2,
    'SWAP6' :2,
    'SWAP7' :2,
    'SWAP8' :2,
    'SWAP9' :2,
    'SWAP10' :2,
    'SWAP11' :2,
    'SWAP12' :2,
    'SWAP13' :2,
    'SWAP14' :2,
    'SWAP15' :2,
    'SWAP16' :2,
    'LOG0' :2,
    'LOG1' :2,
    'LOG2' :2,
    'LOG3' :2,
    'LOG4' :2,
    'CREATE' :2,
    'CALL' :2,
    'CALLCODE' :2,
    'RETURN' :2,
    'DELEGATECALL' :2,
    'CREATE2' :2,
    'STATICCALL' :2,
    'REVERT' :2,
    'INVALID' :2,
    'SELFDESTRUCT' :2
}


class BigramVector:
    def __init__(self, text: str):
        self.text = text

    @staticmethod
    def __indexing(character):
        char1 = hex(ord(character[0]))
        char2 = hex(ord(character[1]))
        result = char1[2:] + char2[2:]
        return int(result, 16)

    def feature_vector(self):
        feature_vector = {}
        sorted_feature_vector = []
        for x in opcodes_dic:
            feature_vector[self.__indexing(x)] = opcodes_dic[x]
        for k in sorted(feature_vector):
            sorted_feature_vector.append("{key}:{value}".format(key=k,value=feature_vector[k]))
        return " ".join(sorted_feature_vector)


with open('SmartContract','r') as f1, open('SmartContractDataset','w') as f2:
    reader = csv.reader(f1)
    writer = csv.writer(f2)
    flag=True
    for r in reader:
        if flag:
            r.append('featureVector')
            writer.writerow((r[8],r[2],r[3],r[4],r[5],r[6],r[7]))
            flag=False
            continue
        bigram_vector_object = BigramVector(text=r[1])
        feature_vector = bigram_vector_object.feature_vector()
        r.append(feature_vector)
        writer.writerow((r[8],r[2],r[3],r[4],r[5],r[6],r[7]))
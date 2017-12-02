import getopt, sys

memory = [] #changing memory
instruction = []
instrName = []
address = []
opcode = []
valid = []
arg1 = []
arg2 = []
arg3 = []
dest = []
src1 = []
src2 = []
PC = 96
numInstructions = 0 #includes BREAK
filler = -1

class disClass:
    def __init__( self ):
        pass

    def disassemble( self ):
        global filler
        global numInstructions
        i = 0
        while True:

            opcode.append(int(instruction[i][1:6],2))
            valid.append(int(instruction[i][0]))

            if instruction[i][0:1] == '0':
                ###work
                instrName.append( '')
                address.append(PC + (i * 4))
                arg1.append(int(instruction[i][6:11],2))
                arg2.append(int(instruction[i][11:16],2))
                arg3.append('')
                dest.append(filler)
                filler-=1
                src1.append(filler)
                filler-=1
                src2.append(filler)
                filler-=1
                numInstructions+=1
                i = i + 1
            else:
                #opcode 0
                if (instruction[i][0:32] == '10000000000000000000000000001101'): #break
                    instrName.append( 'BREAK')
                    address.append(PC + (i * 4))
                    arg1.append(int(instruction[i][6:11],2))
                    arg2.append(int(instruction[i][11:16],2))
                    arg3.append(0)
                    dest.append(filler)
                    filler-=1
                    src1.append(filler)
                    filler-=1
                    src2.append(filler)
                    filler-=1
                    numInstructions+=1
                    i = i + 1
                    break;
                elif opcode[i] == 0:

                    if instruction[i][26:32] == '000000': 
                        if instruction[i][1:32] == '0000000000000000000000000000000':#nop
                            instrName.append( 'NOP')
                            address.append(PC + (i * 4))
                            arg1.append(int(instruction[i][6:11],2))
                            arg2.append(int(instruction[i][11:16],2))
                            arg3.append('')
                            dest.append(filler)
                            filler-=1
                            src1.append(filler)
                            filler-=1
                            src2.append(filler)
                            filler-=1
                            numInstructions+=1
                            i = i + 1
                        else: #SLL Format: SLL rd, rt, sa
                            instrName.append( 'SLL')
                            address.append(PC + (i * 4))
                            arg1.append(int(instruction[i][11:16],2))#rt
                            arg2.append(int(instruction[i][16:21],2))#rd
                            arg3.append(int(instruction[i][21:26],2))#sa
                            dest.append(arg2[i])
                            src1.append(arg1[i])
                            src2.append(filler) 
                            filler-=1
                            numInstructions+=1
                            i = i + 1
                            
                    elif instruction[i][26:32] == '000010': #SRL Format: SRL rd, rt, sa
                        instrName.append( 'SRL')
                        address.append(PC + (i * 4))
                        arg1.append(int(instruction[i][11:16],2))#rt
                        arg2.append(int(instruction[i][16:21],2))#rd
                        arg3.append(int(instruction[i][21:26],2))#sa
                        dest.append(arg2[i])
                        src1.append(arg1[i])
                        src2.append(filler) 
                        filler-=1
                        numInstructions+=1
                        i = i + 1
                        #dfile.write( '\tSRL\tR' + str(rt) + ', R' + str(rd) + ', #' + str(sa) + '\n')
                    
                    elif instruction[i][26:32] == '001000': #JR Format: JR rs
                        instrName.append( 'JR')
                        address.append(PC + (i * 4))
                        arg1.append(int(instruction[i][6:11],2))
                        arg2.append(0)
                        arg3.append(0)
                        dest.append(filler) 
                        filler-=1
                        src1.append(arg1[i])
                        src2.append(filler) 
                        filler-=1
                        numInstructions+=1
                        i = i + 1
                        #dfile.write( '\tJR\tR' + str(rs))

                    elif instruction[i][26:32] == '001010': #MOVZ Format: MOVZ rd, rs, rt
                        instrName.append( 'MOVZ')
                        address.append(PC + (i * 4))
                        arg1.append(int(instruction[i][6:11],2))#rs
                        arg2.append(int(instruction[i][11:16],2))#rt
                        arg3.append(int(instruction[i][16:21],2))#rd
                        dest.append(arg3[i])
                        src1.append(arg1[i])
                        src2.append(arg2[i])
                        numInstructions+=1
                        i = i + 1
                        #dfile.write( '\tMOVZ\tR' + str(rd) + ', R' + str(rs) + ', R' + str(rt) + '\n')

                    elif instruction[i][26:32] == '100000': #ADD Format: ADD rd, rs, rt
                        instrName.append( 'ADD')
                        address.append(PC + (i * 4))
                        arg1.append(int(instruction[i][6:11],2))#rs
                        arg2.append(int(instruction[i][11:16],2))#rt
                        arg3.append(int(instruction[i][16:21],2))#rd
                        dest.append(arg3[i])
                        src1.append(arg1[i])
                        src2.append(arg2[i])
                        numInstructions+=1
                        i = i + 1
           
                    elif instruction[i][26:32] == '100010': #SUB Format: SUB rd, rs, rt
                        instrName.append( 'SUB')
                        address.append(PC + (i * 4))
                        arg1.append(int(instruction[i][6:11],2))#rs
                        arg2.append(int(instruction[i][11:16],2))#rt
                        arg3.append(int(instruction[i][16:21],2))#rd
                        dest.append(arg3[i])
                        src1.append(arg1[i])
                        src2.append(arg2[i])
                        numInstructions+=1
                        i = i + 1
               
                    elif instruction[i][26:32] == '100100': #AND Format: AND rd, rs, rt
                        instrName.append( 'AND')
                        address.append(PC + (i * 4))
                        arg1.append(int(instruction[i][6:11],2))#rs
                        arg2.append(int(instruction[i][11:16],2))#rt
                        arg3.append(int(instruction[i][16:21],2))#rd
                        dest.append(arg3[i])
                        src1.append(arg1[i])
                        src2.append(arg2[i])
                        numInstructions+=1
                        i = i + 1
                 
                    elif instruction[i][26:32] == '100101': #OR Format: OR rd, rs, rt
                        instrName.append( 'OR')
                        address.append(PC + (i * 4))
                        arg1.append(int(instruction[i][6:11],2))#rs
                        arg2.append(int(instruction[i][11:16],2))#rt
                        arg3.append(int(instruction[i][16:21],2))#rd
                        dest.append(arg3[i])
                        src1.append(arg1[i])
                        src2.append(arg2[i])
                        numInstructions+=1
                        i = i + 1

                #opcode 1
                elif opcode[i] == 1: #BLTZ Format: BLTZ rs, offset
                    instrName.append( 'BLTZ')
                    address.append(PC + (i * 4))
                    arg1.append(int(instruction[i][6:11],2))#rs
                    arg2.append(int(instruction[i][11:16],2))#BLTZ
                    arg3.append(int(instruction[i][16:32],2))#offset
                    dest.append(filler) 
                    filler-=1
                    src1.append(arg1[i])
                    src2.append(filler) 
                    filler-=1
                    
                    numInstructions+=1
                    i = i + 1

              
                #opcode 2
                elif opcode[i] == 2: #J
                    instrName.append('J')
                    address.append(PC + (i * 4))
                    arg1.append(int(instruction[i][6:32],2))
                    arg2.append(0)
                    arg3.append(0)
                    dest.append(filler) 
                    filler-=1
                    src1.append(filler) 
                    filler-=1
                    src2.append(filler) 
                    filler-=1
                    numInstructions+=1
                    i = i + 1 
                    
                #opcode 4
                elif opcode[i] == 4: #BEQ Format: BEQ rs, rt, offset
                    instrName.append('BEQ')
                    address.append(PC + (i * 4))
                    arg1.append(int(instruction[i][6:11],2))#rs
                    arg2.append(int(instruction[i][11:16],2))#rt
                    arg3.append(int(instruction[i][16:32],2))#offset
                    dest.append(filler) 
                    filler-=1
                    src1.append(arg1[i])
                    src2.append(arg2[i])
                    numInstructions+=1
                    i = i + 1

                #opcode 8
                elif opcode[i] == 8: #ADDI Format: ADDI rt, rs, immediate
                    instrName.append( 'ADDI')
                    address.append(PC + (i * 4))
                    arg1.append(int(instruction[i][6:11],2))#rs
                    arg2.append(int(instruction[i][11:16],2))#rt
                    arg3.append(int(instruction[i][16:32],2))#immediate
                    if instruction[i][16:17] == '1':
                        arg3[i] = ((arg3[i] ^ 0b1111111111111111) + 1) * -1
                    dest.append(arg2[i])
                    src1.append(arg1[i])
                    src2.append(filler) 
                    filler-=1
                    numInstructions+=1
                    i = i + 1 
                 
                #opcode 0x2b
                elif opcode[i] == 11: #SW Format: SW rt, offset(base)
                    instrName.append( 'SW')
                    address.append(PC + (i * 4))
                    arg1.append(int(instruction[i][6:11],2))#base
                    arg2.append(int(instruction[i][11:16],2))#rt
                    arg3.append(int(instruction[i][16:32],2))#offset
                    dest.append(filler) 
                    filler-=1
                    src1.append(arg2[i])
                    src2.append(arg1[i]) 
                    numInstructions+=1
                    i = i + 1 
                #opcode 0x23
                elif opcode[i] == 3: #LW Format: LW rt, offset(base)
                    instrName.append( 'LW')
                    address.append(PC + (i * 4))
                    arg1.append(int(instruction[i][6:11],2))#base
                    arg2.append(int(instruction[i][11:16],2))#rt
                    arg3.append(int(instruction[i][16:32],2))#offset
                    dest.append(arg2[i])
                    src1.append(arg1[i]) 
                    src2.append(filler) 
                    filler-=1
                    numInstructions+=1
                    i = i + 1
                #opcode 0x1C
                elif opcode[i] == 28: #MUL Format: MUL rd, rs, rt
                    instrName.append( 'MUL')
                    address.append(PC + (i * 4))
                    arg1.append(int(instruction[i][6:11],2))#rs
                    arg2.append(int(instruction[i][11:16],2))#rt
                    arg3.append(int(instruction[i][16:21],2))#rd
                    dest.append(arg3[i])
                    src1.append(arg1[i])
                    src2.append(arg2[i])
                    numInstructions+=1
                    i = i + 1
                
        j = 0
        while i < len(instruction):
            address.append(PC + (i * 4))
            memory.append(int(instruction[i],2))
            if instruction[i][0:1] == '1':
                memory[j] = (((memory[j] ^ 0b11111111111111111111111111111111) + 1) * -1)
            i+=1
            j+=1

    def printDis(self, dfile):
        i = 0
        while i < numInstructions:
            dfile.write( str(instruction[i][0:1]) + ' ' + str(instruction[i][1:6]) + ' ' + str(instruction[i][6:11]) + ' ' + str(instruction[i][11:16]))
            dfile.write( ' ' + str(instruction[i][16:21]) + ' ' + str(instruction[i][21:26]) + ' ' + str(instruction[i][26:32]) + '\t' + str(address[i]))
            
            if instrName[i] in ['MOVZ', 'ADD', 'SUB', 'AND', 'OR', 'MUL']:
                dfile.write( '\t' + instrName[i] + '\tR'+ str(arg3[i]) + ', R' + str(arg1[i]) + ', R' + str(arg2[i]) + '\n')
            elif instrName[i] in ['SLL', 'SRL']:
                dfile.write( '\t' + instrName[i] + '\tR' + str(arg1[i]) + ', R' + str(arg2[i]) + ', #' + str(arg3[i]) + '\n')
            elif instrName[i] in ['BEQ', 'ADDI']:
                dfile.write( '\t' + instrName[i] + '\tR' + str(arg2[i]) + ', R' + str(arg1[i]) + ', #' + str(arg3[i]) + '\n')
            elif instrName[i] in ['SW', 'LW']:
                dfile.write( '\t' + instrName[i] + '\tR' + str(arg2[i]) + ', ' + str(arg3[i]) + '(R' + str(arg1[i]) + ')\n')
            elif instrName[i] == 'BLTZ':
                dfile.write( '\tBLTZ\tR' + str(arg1[i]) + ', #' + str(arg3[i]) + '\n')
            elif instrName[i] == 'J':
                dfile.write( '\tJ\t#' + str(arg1[i]) + '\n')
            elif instrName[i] == 'JR':
                dfile.write( '\tJR\tR' + str(arg1[i]) + '\n')
            elif instrName[i] in ['NOP', 'BREAK', 'Invalid Instruction']:
                dfile.write( '\t' + instrName[i]+ '\n')
            i += 1
        j = 0
        while i < (len(instruction)):
            dfile.write( str(instruction[i][0:32]) + '\t' + str(address[i]) + '\t' + str(memory[j]) + '\n')
            j += 1 
            i += 1

for i in range( len(sys.argv)):
    if(sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
        inputFileName = sys.argv[i+1]
    elif(sys.argv[i] == '-o' and i < (len(sys.argv) -1)):
        outputFileName = sys.argv[i+1]

f = open( inputFileName, 'r')
disFile = open( outputFileName + "_dis.txt", 'w' )
pipelineFile = open( outputFileName + "_pipeline.txt", 'w' )

words = [] 
for line in f:
    instruction.append(line[0:32])
disassembler = disClass()
disassembler.disassemble()
disassembler.printDis(disFile)

########################################
print('INSTRUCTIONS')
print((instruction))
print('OPCODES')
print(opcode)
print('ARG1')
print(arg1)
print('ARG2')
print(arg2)
print('ARG3')
print(arg3)
print('ADDRESS')
print(address)
print('DEST')
print(dest)
print('SRC1')
print(src1 )
print('SRC2')
print(src2)
print('MEMORY')
print(memory)
########################################

class writeBack:
    def __init__(self):
        print('initialized wb')
    def run(self):
        print('wb running')
        if(sim.postALUBuff[1] != -1):
            print('wb destReg index: ' + str(sim.postALUBuff[1]))
            print('wb R index: ' + str(sim.destReg[sim.postALUBuff[1]]))
            
            sim.R[sim.destReg[sim.postALUBuff[1]]] = sim.postALUBuff[0]
            sim.postALUBuff[0] = -1
            sim.postALUBuff[1] = -1
        if(sim.postMemBuff[1] != -1):
            sim.R[sim.destReg[sim.postMemBuff[1]]] = sim.postMemBuff[0]
            sim.postMemBuff[0] = -1
            sim.postMemBuff[1] = -1

class arithmeticLogicUnit:
    
    def __init__(self):
        print('initialized ALU')
    def run(self):
        print('ALU running')
        # pre - uses list from dis for args, expects valid prebuf values or -1s
        # during - gets instruction and decodes which alu instruction to execute. 
        # executes instruction and updates alu post buffer with instruction 
        # index and the result of the alu instruction
        # post - will move second index to position 0 and reset position 1 to -
        #     if sim.opcode[ i ] == 0 and (int(sim.instruction[i],base=2)& specialMask) == 32:       #ADD
        # sim.postALUBuff = [sim.R[ sim.arg1[i] ] + sim.R[ sim.arg2[i] ], i]
        if (sim.preALUBuff[1] != -1):
            i = sim.preALUBuff[1]
            sim.postALUBuff[1] = sim.destReg[i]

            if(sim.instrName[i] == 'SLL'):
                sim.postALUBuff[0] = sim.R[sim.src1Reg[i]] * pow(2,sim.arg3[i])
            elif(sim.instrName[i] == 'SRL'):
                sim.postALUBuff[0] = sim.R[sim.src1Reg[i]] / pow(2,sim.arg3[i])
            elif(sim.instrName[i] == 'ADDI'):
                sim.postALUBuff[0] = sim.R[sim.src1Reg[i]] + sim.arg3[i]
            elif(sim.instrName[i] == 'MUL'):
                sim.postALUBuff[0] = sim.R[sim.src1Reg[i] * sim.R[sim.src2Reg[i]]]
            elif(sim.instrName[i] == 'OR'):
                sim.postALUBuff[0] = sim.R[sim.src1Reg[i] | sim.R[sim.src2Reg[i]]]
            elif(sim.instrName[i] == 'AND'):
                sim.postALUBuff[0] = sim.R[sim.src1Reg[i] & sim.R[sim.src2Reg[i]]]
            elif(sim.instrName[i] == 'SUB'):
                sim.postALUBuff[0] = sim.R[sim.src1Reg[i] - sim.R[sim.src2Reg[i]]]
            elif(sim.instrName[i] == 'ADD'):
                sim.postALUBuff[0] = sim.R[sim.src1Reg[i] + sim.R[sim.src2Reg[i]]]
            ############### rest of alu instructions
            sim.preALUBuff[1] = sim.preALUBuff[0]
            sim.preALUBuff[0] = -1
        else:
            print('not doing ALU stuff')

class memWrite:
    def __init__(self):
        print('initialized MEM')
    def run(self):
        print('MEM running')
#         Input data structure:
# preMemBuff = [-1,-1] # first number is index, second is index
# preMemBuff can hold two instructions per spec

# Output data structure:
# postMemBuff = [-1,-1] # first number is value, second is instr index

    #pre- uses lists from dis for args. Expects valid prebuf values or -1's
        if(sim.preMemBuff[0] != -1):
            i = sim.preMemBuff[0]

            if(sim.instrName[i] == 'LW'):
                address = sim.arg3[i] + sim.R[sim.src1Reg[i]]
                sim.cache.accessMemory(sim.getIndexOfMemAddress(address),-1,False,0)
                #check cache stuff - do cache stuff
                print('lw DEBUG\n address: ' + str(address))
            elif(sim.instrName[i] == 'SW'):
                address = sim.arg3[i] + sim.R[sim.src2Reg[i]]
                sim.cache.accessMemory(sim.getIndexOfMemAddress(address), -1, True, sim.R[sim.src1[i]])
                print('sw DEBUG\n address: ' + str(address))
# Call cache.accessMem(memIndex, i, isSW, sim.R[sim.arg2[i]])   If miss, 
# Cache controller will return with miss on first cycle and will handle 
# the memory access and cache load and should return a hit on second cycle. 
# If hit, will return true with value.  Return hit, update the premem buffer
 # setting premem[0] to premem[1] and setting premem[1] to -1. Then either 
 # write cache for a store or write value obtained from cache to the postmembuff.

#post will leave second index in position 0 and position 1 at -1

        if(sim.preMemBuff[0] != -1):
            i = sim.preMemBuff[1]
            if(sim.instrName[i] == 'LW'):
                #check cache stuff - do cache stuff
                print('lw DEBUG')
            #####storeword stuff

class issueUnit:
    def __init__(self):
        print('initialized issue')
    def run(self):
        print('issue running')
        print('issue stuff')

        issueMe = True
        numIssued = 0
        numInPreIssueBuff = 0
        currIndex = -1
        current = 0

        for i in range(4):
            if(sim.preIssueBuff[i] != -1):
                numInPreIssueBuff += 1

        # 2. process instructions in preissue buff in 0-3 order. look
        # for hazards of all types between mostly adjacent instructions
        ##WAR CHECK

        while(numIssued < 2 and numInPreIssueBuff > 0 and current < 4):
            currIndex = sim.preIssueBuff[current]
            
            ## CHECK FOR ROOM IN BUFFERS
            if sim.isMemOp(currIndex) and not -1 in sim.preMemBuff:
                issueMe = False
            elif not sim.isMemOp(currIndex) and not -1 in sim.preALUBuff:
                issueMe = False

            ## WAR CHECK    
            if current > 0:
                for i in range(0,current):
                    if (sim.destReg[currIndex] == sim.src1Reg[sim.preIssueBuff[i]] or sim.destReg[current] == sim.src2Reg[sim.preIssueBuff[i]]):
                        issueMe = False
                        break
            if sim.isMemOp(currIndex):
                for i in range(0, len(sim.preMemBuff)):
                    if sim.preMemBuff[i] != -1:
                        if sim.destReg[currIndex] == sim.src1Reg[sim.preMemBuff[i]] or sim.destReg[currIndex] == sim.src2Reg[sim.preMemBuff[i]]:
                            issueMe = False
                            break
            else:
                for i in range(0, len(sim.preALUBuff)):
                    if sim.preALUBuff[i] != -1:
                        if sim.destReg[currIndex] == sim.src1Reg[sim.preALUBuff[i]] or sim.destReg[currIndex] == sim.src2Reg[sim.preALUBuff[i]]:
                            issueMe = False
                            break
            ## RAW CHECK
            if current > 0:
                for i in range(0,current):
                    if (sim.src1Reg[currIndex] == sim.destReg[sim.preIssueBuff[i]] or sim.src2Reg[currIndex] == sim.destReg[sim.preIssueBuff[i]]):
                        issueMe = False
                        break
            
            for i in range(0, len(sim.preMemBuff)):
                if sim.preMemBuff[i] != -1:
                    if sim.src1Reg[currIndex] == sim.destReg[sim.preMemBuff[i]] or sim.src2Reg[currIndex] == sim.destReg[sim.preMemBuff[i]]:
                        issueMe = False
                        break
            for i in range(0, len(sim.preALUBuff)):
                if sim.preALUBuff[i] != -1:
                    if sim.src1Reg[currIndex] == sim.destReg[sim.preALUBuff[i]] or sim.src2Reg[currIndex] == sim.destReg[sim.preALUBuff[i]]:
                        issueMe = False
                        break
            if sim.postALUBuff[1] != -1:
                if sim.src1Reg[currIndex] == sim.destReg[sim.postALUBuff[1]] or sim.src2Reg[currIndex] == sim.destReg[sim.postALUBuff[1]]:
                    #found RAW in post ALU Buffer
                    issueMe = False
            if sim.postMemBuff[1] != -1:
                if sim.src1Reg[currIndex] == sim.destReg[sim.postMemBuff[1]] or sim.src2Reg[currIndex] == sim.destReg[sim.postMemBuff[1]]:
                    #found RAW in post ALU Buffer
                    issueMe = False
           
            ## WAW CHECK
            for i in range(0, len(sim.preMemBuff)):
                if sim.preMemBuff[i] != -1:
                    if sim.destReg[currIndex] == sim.destReg[sim.preMemBuff[i]]:
                        issueMe = False
                        break
            for i in range(0, len(sim.preALUBuff)):
                if sim.preALUBuff[i] != -1:
                    if sim.destReg[currIndex] == sim.destReg[sim.preALUBuff[i]]:
                        issueMe = False
                        break
            if sim.postALUBuff[1] != -1:
                if sim.destReg[currIndex] == sim.destReg[sim.postALUBuff[1]]:
                    #found RAW in post ALU Buffer
                    issueMe = False
            if sim.postMemBuff[1] != -1:
                if sim.destReg[currIndex] == sim.destReg[sim.postMemBuff[1]]:
                    #found RAW in post ALU Buffer
                    issueMe = False
        
            ##ENFORCE ORDERING OF LW SW
            #Enforce ordering of LWs and SWs so we make sure all stores are done before loads
            
            ##ISSUE AND MOVE INSTRUCTIONS DOWN ONE LEVEL
            if issueMe:
                numIssued += 1
                #copy the instruction to the appropriate buffer
                #the assumption here is that we will ahve a -1 i the right spot
                if sim.isMemOp(currIndex):
                    sim.preMemBuff[sim.preMemBuff.index(-1)] = currIndex
                else:
                    sim.preALUBuff[sim.preALUBuff.index(-1)] = currIndex

                #move the instructions in the preissue buff down one level
                sim.preIssueBuff[0:current] = sim.preIssueBuff[0:current]
                print "pre" + str(sim.preALUBuff[current + 1])
                sim.preIssueBuff[current:3] = sim.preIssueBuff[current+1:]
                sim.preIssueBuff[3] = -1
                numInPreIssueBuff -= 1
            else:
                current += 1

class instructionFetch:
    def __init__(self):
        print('initialized fetch')
    def run(self):
        print('fetch running')
        # pre - have all of the lists from the disassembler
        index = (sim.PC - 96) / 4
        print('index = ' + str(index))
        
        hit, data = sim.cache.accessMemory(-1, index, 0, 0)
        print('hit: ' + str(hit))
        print('data: ' + str(data))
        if(hit):
            #if(branch or jump):
                #do stuff
            sim.preIssueBuff[0] = index
            print('data: ' + str(data))
            sim.PC += 4

            #try to load another instruction
            hit, data = sim.cache.accessMemory(-1, index + 1, False, 0)
            if(hit):
                #if(branch or jump):
                    #do stuff
                sim.preIssueBuff[1] = index + 1
                print('data: ' + str(data))
                sim.PC += 4

        # during - We will fetch tup to two empty slots in the 
        # preissue buffer. We get an instruction, check in cache for it,
        # If hit we will determine if it is a branch or jump 
        # instructios. If is a branch instruction will check for 
        # hazards and if none perform the branch instruction. 
        # Jump done without checking.  The branch will never get 
        # posted to the pre issue buffer.  Checks for break  
        # instruction and if found perfoms clean up making  sure 
        # all instructions finish. Else we don't have a break 
        # instruction. If we can't get the first instruction out 
        # of cache we can't fetch the next instruction.
        if(sim.cycle > 9): #for checking
            return False
        else:
            return True
        

        # post - when the correct number of instructions fetched,
        # # the entire program will cycle and start execution over 
        # # again

class cacheUnit:
    cacheSet = [[[0,0,0,0,0],[0,0,0,0,0]], #valid,dirty,tag,data,data
                [[0,0,0,0,0],[0,0,0,0,0]],
                [[0,0,0,0,0],[0,0,0,0,0]],
                [[0,0,0,0,0],[0,0,0,0,0]]]
    lruBit = [0,0,0,0] #one for each SET
    tagMask = int('00000000000000000000000011111111',2)
    # 96 = 01100000 set 0, tag 3
    setMask = int('0011111',2)
    justMissedList = -1

    def __init__(self):
        print('cache initialized')

    def flush(self):
        print('cache flush function')
        # Flush:
        # Writes out all dirty blocks to memory at the 
        # conclusion of execution
        for s in range(4):
            if(self.cacheSet[s][0][1] == 1 or self.cacheSet[s][1][1] == 1): 
                pass #write to memory
                wbAddr

    def accessMemory(self, memIndex, instrIndex, isWriteTomem, dataToWrite):
        #figure out the alignment
        if(instrIndex != -1):
            address = (instrIndex * 4) + 96
        else:
            address = (memIndex * 4) + 96

        if(address % 8 == 0): #address 96+n8
            dataword = 0 #block 0 was the address
            address1 = address
            address2 = address + 4
        else: #address != 96+n8
            dataword = 1 #block 1 was the address
            address1 = address - 4
            address2 = address

        data1 = sim.instruction[(address1 - 96) / 4]
        data2 = sim.instruction[(address2 - 96) / 4]

        #4
        if(isWriteTomem and dataword == 0):
            data1 = dataToWrite
        elif(isWriteTomem and dataword == 1):
            data2 = dataToWrite

        #5. decode the address of word 0 into cache address
        tag =  (address1 & self.tagMask)
        setNum = (tag & self.setMask) >> 3
        tag = tag >> 5

        #6. look in cache and see if the address is in either block
        hit = False
        if(self.cacheSet[setNum][0][2] == tag):
            assocblock = 0
            hit = True 
        elif(self.cacheSet[setNum][1][2] == tag):
            assocblock = 1
            hit = True

        if(hit and isWriteTomem):
            #update dirty bit
            self.cacheSet[setNum][assocblock][1] = 1 
            #update set lru bit
            self.lruBit[setNum] = (assocblock + 1) % 2
            #write data to cache
            self.cacheSet[setNum][assocblock][dataword + 3] = dataToWrite
            return True, self.cacheSet[setNum][assocblock][dataword + 3]
        #8.
        elif(hit and not isWriteTomem):
            #update set lru bit
            self.lruBit[setNum] = (assocblock + 1) % 2
            return True, self.cacheSet[setNum][assocblock][dataword + 3]
        #9. 
        elif(not hit):
            if(self.justMissedList != address1):
                self.justMissedList = address1
                print('just missed: ' + str(self.justMissedList))
                return False, 0
            else: #second miss
                if self.cacheSet[setNum][ self.lruBit[setNum] ][1] == 1:
                    # write back the memory address asociated with the block
                    wbAddr =  self.cacheSet[setNum][ self.lruBit[setNum] ][2] #tag
                    # modify tag to get back to the original address, remember all addresses are inherently word aligned
                    # lower 2 bits are zero !!!!
                    wbAddr = (wbAddr << 5) +( setNum << 3)

                    # we will, we better,  only have dirty cache entries for data mem, not instructions
                    # update data mem locations!
                    # if the cache tag: set gives us a double word aligned value ie. 96,104,
                    # Lets say that word 0 is the last instruction and word on is the first data element
                    # we would only want to update the second word
                    # But if lets say we have two data elemeents, then the cache would have two data element and we would write
                    # back both even if one was dirty.  This takes care of the boundry condition.

                    if( wbAddr >= (sim.numInstructions  *4) + 96 ):
                        sim.memory[ sim.getIndexOfMemAddress(wbAddr) ] = self.cacheSet[setNum][ self.lruBit[setNum] ][3]
                    if( wbAddr+4 >= (sim.numInstructions  *4) + 96 ):
                        sim.memory[ sim.getIndexOfMemAddress(wbAddr+4) ] = self.cacheSet[setNum][ self.lruBit[setNum] ][4]
                    # now update the cache flag bits
                self.cacheSet[setNum][ self.lruBit[setNum] ][0] = 1 #valid  we are writing a block
                self.cacheSet[setNum][ self.lruBit[setNum] ][1] = 0 #reset the dirty bit
                if( isWriteTomem ):
                    self.cacheSet[setNum][ self.lruBit[setNum] ][1] = 1 #dirty if is data mem is dirty again, intruction mem never dirty
                # update both words in the actual cache block in set
                self.cacheSet[setNum][ self.lruBit[setNum] ][2] = tag #tag
                self.cacheSet[setNum][ self.lruBit[setNum] ][3] = data1 #data
                self.cacheSet[setNum][ self.lruBit[setNum] ][4] = data2 #nextData
                self.lruBit[setNum] = (self.lruBit[setNum] + 1) % 2 # set lru to show block is recently used
                return [True, self.cacheSet[setNum][(self.lruBit[setNum] + 1) % 2][dataword+3] ]   # dataword was the actual word thatgenerated the hit

class simClass:
    instruction = []
    opcode = []
    memory = []
    validInstr = []
    address = []
    numInstructions = 0
    instrName = []
    arg1 = []
    arg2 = []
    arg3 = []
    destReg = []
    src1Reg = []
    src2Reg = []
    cycle = 1
    PC = 96
    R = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] #registers 0-32 
    WB = writeBack()
    ALU = arithmeticLogicUnit()
    MEM = memWrite()
    issue = issueUnit()
    fetch = instructionFetch()
    cache = cacheUnit()

    preMemBuff = [-1,-1] #first number is index, second is index
    postMemBuff = [-1,-1] #first number is value, scond is instruction index

    preALUBuff = [-1,-1]#first number is index, second is index, 2 instructions
    postALUBuff = [-1,-1]#first number is value, second is instr index

    preIssueBuff = [-1,-1,-1,-1] # list of 4 instruction indices

    def __init__( self, instrs, opcodes, mem, valids, addrs, arg1, arg2, arg3, numInstrs, dest, src1, src2, instrNa ):
        self.instruction = instrs
        self.opcode = opcodes
        self.memory = mem
        self.validInstr = valids
        self.address = addrs
        self.numInstructions = numInstrs
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.destReg = dest
        self.src1Reg = src1
        self.src2Reg = src2
        self.instrName = instrNa

    def printState(self):

        dataAddress = 96 + (self.numInstructions * 4)
        formattedInstr = ['','','','','','','','','','']
        indices = []
        for i in range(4):
            indices.append((self.preIssueBuff[i]))

        indices.append(self.preALUBuff[0])
        indices.append(self.preALUBuff[1])
        indices.append(self.postALUBuff[0])
        indices.append(self.preMemBuff[0])
        indices.append(self.preMemBuff[1])
        indices.append(self.postMemBuff[0])

        print('indices: ' + str(indices))

        for i in range(10):
            if indices[i] != -1:
                if instrName[indices[i]] in ['MOVZ', 'ADD', 'SUB', 'AND', 'OR', 'MUL']:
                    formattedInstr[indices[i]] = instrName[indices[i]] + '\tR'+ str(arg3[indices[i]]) + ', R' + str(arg1[indices[i]]) + ', R' + str(arg2[indices[i]])
                elif instrName[indices[i]] in ['SLL', 'SRL']:
                    formattedInstr[indices[i]] = instrName[indices[i]] + '\tR' + str(arg1[indices[i]]) + ', R' + str(arg2[indices[i]]) + ', #' + str(arg3[indices[i]]) 
                elif instrName[indices[i]] in ['BEQ', 'ADDI']:
                    formattedInstr[indices[i]] = instrName[indices[i]] + '\tR' + str(arg2[indices[i]]) + ', R' + str(arg1[indices[i]]) + ', #' + str(arg3[indices[i]]) 
                elif instrName[indices[i]] in ['SW', 'LW']:
                    formattedInstr[i] = instrName[indices[i]] + '\tR' + str(arg2[indices[i]]) + ', ' + str(arg3[indices[i]]) + '(R' + str(arg1[indices[i]]) 
                elif instrName[indices[i]] == 'BLTZ':
                    formattedInstr[indices[i]] =  'BLTZ\tR' + str(arg1[indices[i]]) + ', #' + str(arg3[indices[i]]) 
                elif instrName[indices[i]] == 'J':
                    formattedInstr[i] =  'J\t#' + str(arg1[indices[i]]) 
                elif instrName[indices[i]] == 'JR':
                    formattedInstr[i] = 'JR\tR' + str(arg1[indices[i]])
                elif instrName[indices[i]] in ['NOP', 'BREAK', 'Invalid Instruction']:
                    formattedInstr[indices[i]] = instrName[indices[i]]

        print('--------------------\n' 
            + 'Cycle:' + str(self.cycle)
            + '\n\nPre-Issue Buffer:\n'
            + '\tEntry 0:\t' + formattedInstr[0] + '\n'
            + '\tEntry 1:\t' + formattedInstr[1] + '\n'
            + '\tEntry 2:\t' + formattedInstr[2] + '\n'
            + '\tEntry 3:\t' + formattedInstr[3] + '\n'
            + 'Pre_ALU Queue:\n'
            + '\tEntry 0:\t' + formattedInstr[4] + '\n'
            + '\tEntry 1:\t' + formattedInstr[5] + '\n'
            + 'Post_ALU Queue:\n'
            + '\tEntry 0:\t' + formattedInstr[6] + '\n'
            + 'Pre_MEM Queue:\n'
            + '\tEntry 0:\t' + formattedInstr[7] + '\n'
            + '\tEntry 1:\t' + formattedInstr[8] + '\n'
            + 'Post_MEM Queue:\n'
            + '\tEntry 0:\t' + formattedInstr[9] + '\n')

        print('Registers' 
            + '\nR00:\t' + str(self.R[0]) + '\t' + str(self.R[1]) + '\t' + str(self.R[2]) + '\t' + str(self.R[3]) 
            + '\t' + str(self.R[4]) + '\t' + str(self.R[5]) + '\t' + str(self.R[6]) + '\t' + str(self.R[7])
            + '\nR08:\t' + str(self.R[8]) + '\t' + str(self.R[9]) + '\t' + str(self.R[10]) + '\t' + str(self.R[11]) 
            + '\t' + str(self.R[12]) + '\t' + str(self.R[13]) + '\t' + str(self.R[14]) + '\t' + str(self.R[15])
            + '\nR16:\t' + str(self.R[16]) + '\t' + str(self.R[17]) + '\t' + str(self.R[18]) + '\t' + str(self.R[19]) 
            + '\t' + str(self.R[20]) + '\t' + str(self.R[21]) + '\t' + str(self.R[22]) + '\t' + str(self.R[23])
            + '\nR24:\t' + str(self.R[24]) + '\t' + str(self.R[25]) + '\t' + str(self.R[26]) + '\t' + str(self.R[27]) 
            + '\t' + str(self.R[28]) + '\t' + str(self.R[29]) + '\t' + str(self.R[30]) + '\t' + str(self.R[31])
            + '\n')
            
        print('Cache\n'
            + 'Set 0: LRU=' + str(self.cache.lruBit[0]) + '\n'
            + '\tEntry 0: [('+ str(self.cache.cacheSet[0][0][0]) + ', '+ str(self.cache.cacheSet[0][0][1]) 
            + ', '+ str(self.cache.cacheSet[0][0][2]) + ') <'+ str(self.cache.cacheSet[0][0][3]) + ', '
            + str(self.cache.cacheSet[0][0][4]) + '>]\n' 
            + '\tEntry 1: [('+ str(self.cache.cacheSet[0][1][0]) + ', '+ str(self.cache.cacheSet[0][1][1]) 
            + ', '+ str(self.cache.cacheSet[0][1][2]) + ') <'+ str(self.cache.cacheSet[0][1][3]) + ', '
            + str(self.cache.cacheSet[0][1][4]) + '>]\n' 
            + 'Set 1: LRU=' + str(self.cache.lruBit[1]) + '\n'
            + '\tEntry 0: [('+ str(self.cache.cacheSet[1][0][0]) + ', '+ str(self.cache.cacheSet[1][0][1]) 
            + ', '+ str(self.cache.cacheSet[1][0][2]) + ') <'+ str(self.cache.cacheSet[1][0][3]) + ', '
            + str(self.cache.cacheSet[1][0][4]) + '>]\n' 
            + '\tEntry 1:  [('+ str(self.cache.cacheSet[1][1][0]) + ', '+ str(self.cache.cacheSet[1][1][1]) 
            + ', '+ str(self.cache.cacheSet[1][1][2]) + ') <'+ str(self.cache.cacheSet[1][1][3]) + ', '
            + str(self.cache.cacheSet[1][1][4]) + '>]\n' 
            + 'Set 2: LRU=' + str(self.cache.lruBit[2]) + '\n'
            + '\tEntry 0: [('+ str(self.cache.cacheSet[2][0][0]) + ', '+ str(self.cache.cacheSet[2][0][1]) 
            + ', '+ str(self.cache.cacheSet[2][0][2]) + ') <'+ str(self.cache.cacheSet[2][0][3]) + ', '
            + str(self.cache.cacheSet[2][0][4]) + '>]\n' 
            + '\tEntry 1: [('+ str(self.cache.cacheSet[2][1][0]) + ', '+ str(self.cache.cacheSet[2][1][1]) 
            + ', '+ str(self.cache.cacheSet[2][1][2]) + ') <'+ str(self.cache.cacheSet[2][1][3]) + ', '
            + str(self.cache.cacheSet[2][1][4]) + '>]\n'
            + 'Set 3: LRU=' + str(self.cache.lruBit[0]) + '\n'
            + '\tEntry 0:  [('+ str(self.cache.cacheSet[3][0][0]) + ', '+ str(self.cache.cacheSet[3][0][1]) 
            + ', '+ str(self.cache.cacheSet[3][0][2]) + ') <'+ str(self.cache.cacheSet[3][0][3]) + ', '
            + str(self.cache.cacheSet[3][0][4]) + '>]\n' 
            + '\tEntry 1: [('+ str(self.cache.cacheSet[3][1][0]) + ', '+ str(self.cache.cacheSet[3][1][1]) 
            + ', '+ str(self.cache.cacheSet[3][1][2]) + ') <'+ str(self.cache.cacheSet[3][1][3]) + ', '
            + str(self.cache.cacheSet[3][1][4]) + '>]\n' )

        i = 0
        while i < len(self.memory):
            if( i % 8 == 0 and i == 0):
                print(str(dataAddress) + ':\t' + str(self.memory[i])),
            elif( i % 8 == 0 and not i == 0):
                print('\n' + str(dataAddress) + ':\t' + str(self.memory[i])),
            else: #not a multiple of 8
                print('\t' + str(self.memory[i])),
            i += 1
            dataAddress += 4


    def isMemOp(self, index):
        if self.instrName[index] in ['LW', 'SW']:
            return True
        return False
    def getIndexOfMemAddress(self, wbAddr):
        return ((wbAddr - (96 + (4 * self.numInstructions)))/4)
      
    def run( self):
        go = True
        while go:
            self.WB.run()
            self.ALU.run()
            self.MEM.run()
            self.issue.run()
            go = self.fetch.run()
            self.printState()
            self.cycle+=1
            

sim = simClass(instruction, opcode, memory, valid, address, arg1, arg2, arg3, numInstructions, 
    dest, src1, src2, instrName)
sim.run()
                       
    # f.close()

    # simFile.close()
    # disFile.close()


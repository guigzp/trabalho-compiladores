import math
import os

# search_space = ['-targetlibinfo', ' -tti', ' -tbaa', ' -scoped-noalias', ' -assumption-cache-tracker', ' -profile-summary-info', ' -forceattrs', ' -inferattrs', ' -callsite-splitting', ' -ipsccp', ' -called-value-propagation', ' -globalopt', ' -domtree', ' -mem2reg', ' -deadargelim', ' -domtree', ' -basicaa', ' -aa', ' -loops', ' -lazy-branch-prob', ' -lazy-block-freq', ' -opt-remark-emitter', ' -instcombine', ' -simplifycfg', ' -basiccg', ' -globals-aa', ' -prune-eh', ' -inline', ' -functionattrs', ' -argpromotion', ' -domtree', ' -sroa', ' -basicaa', ' -aa', ' -memoryssa', ' -early-cse-memssa', ' -speculative-execution', ' -domtree', ' -basicaa', ' -aa', ' -lazy-value-info', ' -jump-threading', ' -lazy-value-info', ' -correlated-propagation', ' -simplifycfg', ' -domtree', ' -basicaa', ' -aa', ' -loops', ' -lazy-branch-prob', ' -lazy-block-freq', ' -opt-remark-emitter', ' -instcombine', ' -libcalls-shrinkwrap', ' -loops', ' -branch-prob', ' -block-freq', ' -lazy-branch-prob', ' -lazy-block-freq', ' -opt-remark-emitter', ' -pgo-memop-opt', ' -domtree', ' -basicaa', ' -aa', ' -loops', ' -lazy-branch-prob', ' -lazy-block-freq', ' -opt-remark-emitter', ' -tailcallelim', ' -simplifycfg', ' -reassociate', ' -domtree', ' -loops', ' -loop-simplify', ' -lcssa-verification', ' -lcssa', ' -basicaa', ' -aa', ' -scalar-evolution', ' -loop-rotate', ' -licm', ' -loop-unswitch', ' -simplifycfg', ' -domtree', ' -basicaa', ' -aa', ' -loops', ' -lazy-branch-prob', ' -lazy-block-freq', ' -opt-remark-emitter', ' -instcombine', ' -loop-simplify', ' -lcssa-verification', ' -lcssa', ' -scalar-evolution', ' -indvars', ' -loop-idiom', ' -loop-deletion', ' -loop-unroll', ' -mldst-motion', ' -aa', ' -memdep', ' -lazy-branch-prob', ' -lazy-block-freq', ' -opt-remark-emitter', ' -gvn', ' -basicaa', ' -aa', ' -memdep', ' -memcpyopt', ' -sccp', ' -domtree', ' -demanded-bits', ' -bdce', ' -basicaa', ' -aa', ' -loops', ' -lazy-branch-prob', ' -lazy-block-freq', ' -opt-remark-emitter', ' -instcombine', ' -lazy-value-info', ' -jump-threading', ' -lazy-value-info', ' -correlated-propagation', ' -domtree', ' -basicaa', ' -aa', ' -memdep', ' -dse', ' -loops', ' -loop-simplify', ' -lcssa-verification', ' -lcssa', ' -aa', ' -scalar-evolution', ' -licm', ' -postdomtree', ' -adce', ' -simplifycfg', ' -domtree', ' -basicaa', ' -aa', ' -loops', ' -lazy-branch-prob', ' -lazy-block-freq', ' -opt-remark-emitter', ' -instcombine', ' -barrier', ' -elim-avail-extern', ' -basiccg', ' -rpo-functionattrs', ' -globalopt', ' -globaldce', ' -basiccg', ' -globals-aa', ' -float2int', ' -domtree', ' -loops', ' -loop-simplify', ' -lcssa-verification', ' -lcssa', ' -basicaa', ' -aa', ' -scalar-evolution', ' -loop-rotate', ' -loop-accesses', ' -lazy-branch-prob', ' -lazy-block-freq', ' -opt-remark-emitter', ' -loop-distribute', ' -branch-prob', ' -block-freq', ' -scalar-evolution', ' -basicaa', ' -aa', ' -loop-accesses', ' -demanded-bits', ' -lazy-branch-prob', ' -lazy-block-freq', ' -opt-remark-emitter', ' -loop-vectorize', ' -loop-simplify', ' -scalar-evolution', ' -aa', ' -loop-accesses', ' -loop-load-elim', ' -basicaa', ' -aa', ' -lazy-branch-prob', ' -lazy-block-freq', ' -opt-remark-emitter', ' -instcombine', ' -simplifycfg', ' -domtree', ' -loops', ' -scalar-evolution', ' -basicaa', ' -aa', ' -demanded-bits', ' -lazy-branch-prob', ' -lazy-block-freq', ' -opt-remark-emitter', ' -slp-vectorizer', ' -opt-remark-emitter', ' -instcombine', ' -loop-simplify', ' -lcssa-verification', ' -lcssa', ' -scalar-evolution', ' -loop-unroll', ' -lazy-branch-prob', ' -lazy-block-freq', ' -opt-remark-emitter', ' -instcombine', ' -loop-simplify', ' -lcssa-verification', ' -lcssa', ' -scalar-evolution', ' -licm', ' -alignment-from-assumptions', ' -strip-dead-prototypes', ' -globaldce', ' -constmerge', ' -domtree', ' -loops', ' -branch-prob', ' -block-freq', ' -loop-simplify', ' -lcssa-verification', ' -lcssa', ' -basicaa', ' -aa', ' -scalar-evolution', ' -branch-prob', ' -block-freq', ' -loop-sink', ' -lazy-branch-prob', ' -lazy-block-freq', ' -opt-remark-emitter', ' -instsimplify', ' -div-rem-pairs', ' -simplifycfg', ' -verify']

search_space = ['-targetlibinfo', ' -tti', ' -tbaa', ' -scoped-noalias']

size_search_space = len(search_space)

baseline = [1 for _ in range(size_search_space)]



#  speedup = tempo de O3 / tempo da otimização
#  melhoria =  (1 - speedup) * 100
#  Contexto: seleção de otimizações

def flags_baseline():
    flags = ''
    for x in range(size_search_space):
        if baseline[x] == 1:
            flags += search_space[x]
    return flags

def calculate_time(flags):
    os.system('OPT=\"'+ flags +'\" ./run.sh')
    f = open('run.log', 'r')
    f.readline()
    time = float(f.readline().split('\t')[3].strip())
    f.close()
    return time

def find_index_most_negative(tuples):
    smaller_number = math.inf
    index = 0
    for element in tuples:
        if element[0] < smaller_number:
            smaller_number = element[0]
            index = element[1]
    return index

def ie_algorithm():
    global baseline
    continue_ie = True
    cont = 0
    while(continue_ie):
        baseline_time = calculate_time(flags_baseline())
        rip_combinations = []
        for x in range(size_search_space):
            if baseline[x] == 1:
                baseline[x] = 0
                time = calculate_time(flags_baseline())
                rip = ((time - baseline_time) / baseline_time) * 100
                rip_combinations.append([rip, x])
                baseline[x] = 1
        negative_rip = list(filter(lambda x: x[0] < 0, rip_combinations))
        if len(negative_rip) > 0:
            index_most_negative = find_index_most_negative(negative_rip)
            baseline[index_most_negative] = 0
        else:
            continue_ie = False
        rip_combinations.clear()
    flags = ''
    for x in range(size_search_space):
        if baseline[x] == 1:
            flags += search_space[x]
            cont += 1
    return flags, cont


flags, amount_flags = ie_algorithm()

print('Quantidade de Flags Originais: ', size_search_space)
print('Quantidade de Flags do Conjunto de Otimização: ', amount_flags)
print('Diferença: ', size_search_space - amount_flags)
print('Flags do Conjunto de Otimização: ', flags)
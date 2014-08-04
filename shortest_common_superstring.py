from collections import defaultdict

def ShortestCommonSuperstring(originalSeqs):
  paths = defaultdict(set)
  paths[0] =  { '' }
  while paths:
    minLength = min(paths.keys())
    while paths[minLength]:
      candidate = paths[minLength].pop()
      seqAdded = False
      for seq in originalSeqs:
        if seq in candidate:
          continue
        seqAdded = True
        for i in reversed(range(len(seq)+1)):
          if candidate.endswith(seq[:i]):
            newCandidate = candidate + seq[i:]
            paths[len(newCandidate)].add(newCandidate)
      if not seqAdded:  
        return candidate
    del paths[minLength]

seqs = []
for line in open("input.txt", "r"):
  seqs.append(line.rstrip())

output = open("output.txt", "w")
output.write(ShortestCommonSuperstring(seqs))
output.close


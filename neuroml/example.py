import loaders
doc = loaders.NeuroMLLoader.load('Purk2M9s.nml')

mycell = doc.cells[0]

#extract the morphology:
my_morphology = mycell.morphology

#randomly  change a segment id:
my_morphology.segments[33].id = 'random_test'

newcell = .Cell()
newcell.id = "some random cell"

new_morphology = nml.Morphology()
newcell.morphology = new_morphology

new_morphology.id = 'some random morphology'

#add a few segments to that morphology:
for i in range(10):
    segment = nml.Segment()
    segment.id = "some random segment"
    new_morphology.add_segment(segment)

doc.add_cell(newcell)

f = open('test.xml','w')
doc.export(f,0)

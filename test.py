#Import a csv file into a dictionary
#dictionary shoould look like VL1..VL15 like level columns, then [W]Default, than any number of
#[A],[N],[S] attribute field and [H] hierarchy with the conected [W]\Hierarchy name field
import os,csv
source_path='C:\\Users\\S4U39F\\mzs\\Python\\My Projects\\Samples\\'
print(source_path)
dimension_csv = open( source_path+'test.csv')
dimension_csv_reader = csv.DictReader(dimension_csv, delimiter = ';')
dimension_csv_dict =list(dimension_csv_reader)
#create additional elements in the dictionary for all line
#create the followwing elemens
#        *element_in_row
#        *element_level_in_row
row_id=0
normalized_csv=[]
for element in dimension_csv_dict:
    row_id+=1
    element_value=''
    for key, value in element.items():
        if value.lower() !='' and key[:2].lower()=='vl':
            if element_value == '':
                print(value,key[2:], end= ' ')
                normalized_csv.append({'element_in_row':value, 'row_id':row_id,'element_level_in_row':key[2:]})
                element_value=value
            else:
                print('Invalid row: '+str(row_id)+' Multiple element in one row.',end='\n')
    print('\n')

for i in normalized_csv:
    print(i)

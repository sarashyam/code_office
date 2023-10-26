''' 
26/10/2023
This is a program which counts the number of oval and textboxes present in a pdf file , 
it also count the similar color type of oval and textboxes and writes in a txt file whose name is same as the name of pdf file
'''

import fitz                         # to extract the pdf file
import os
import webcolors as wb             # to convert rgb color to color name

# class myexp(Exception):
#     def __init__(self, message="color not found"):
#         super().__init__(message)

c_count = 0                                            # to count ovals
t_count = 0                                            # to count textboxes
o_list =[]                                             # stores the diffrent rgb tuples of oval
t_list =[]                                             # stores the diffrent rgb tuples of textboxes

# --------------------this block counts the total number of oval and textboxes-------------------------------------------
def print_count(pdf_path,fname): 
    global c_count # accessing the global variables declared before
    global t_count
    global o_list 
    global t_list

    doc = fitz.open(pdf_path)                                                     # to open the path where the pdf is located
    c = (5, 'Circle')                                                             # annotation type of oval can be represented as (5, 'Circle')
    t = (2, 'FreeText', 'FreeText')                                                # annotation type of textbox can be represented as (2, 'FreeText', 'FreeText')

    for page_num in range(len(doc)):                                             # to count number of pages in the pdf file
        page = doc[page_num]                                                      # accessing the page
        for annotation in page.annots():                                         # iterating through the annotations present in the page
            typ = annotation.type                                                # type of the annotation 

            if "Circle" in typ:                                                 # typ == c: checking if circle is present in the annotation type for oval
                c_count+=1 # counting the number of ovals
                clr = annotation.colors                                         # to get the annotation color and returns the fill color and stroke color in tuple format  like {'stroke': None, 'fill': (0.0, 0.25099998712539673, 0.25099998712539673),
                        #print(clr)
                val = clr['fill']                                                 # to get the tuple of fill key to access oval color
                #o_list.append(val)
                #print(val)
                if val != None:
                            rgb_normalized = clr['fill'] # return in (0.0, 0.25099998712539673, 0.25099998712539673)
                            rgb_original = tuple(int(round(component * 255, 1)) for component in rgb_normalized) # converting to rgb format (0, 64, 64) 
                            #print(f"rgb converted {rgb_original} value ")
                            o_list.append(rgb_original)                            # appending the value to oval list
                             

            # doing the same as oval but difference is textbox takes the color of stroke not the fill
            if 2 in typ:                                                        #typ == t: checking if 2 is present in the annotation type for textbox
                t_count+=1
                clr = annotation.colors                                         # to get the annotation color
                        #print(clr)
                val = clr['stroke']
                #o_list.append(val)
                #print(val)
                if val != None:
                            rgb_normalized = clr['stroke']
                            rgb_original = tuple(int(round(component * 255, 1)) for component in rgb_normalized)
                            #print(f"rgb converted {rgb_original} value ")
                            t_list.append(rgb_original)



    with open(fname, "a") as file: # writing the total number of oval and textbox count
                    file.write(f"oval count  = {c_count}   textbox count  = {t_count} \n ")

    doc.close() # closing the document once opened

#-------------------------------------------------------------------------------------------
    # print(f"  oval {o_list}")
    # print(f" textbox  {t_list}")



# just for reference------------------------------------
# def color_count(pdf_path,fname):
#     c_count = 0
#     t_count = 0

#     doc = fitz.open(pdf_path)
#     c = (5, 'Circle')
#     t = (2, 'FreeText', 'FreeText')

#     for page_num in range(len(doc)):
#         page = doc[page_num]
#         for annotation in page.annots():
#             typ = annotation.type

#             if "Circle" in typ:     # typ == c:
#                 c_count+=1

#             if 2 in typ:            #typ == t:
#                 t_count+=1

#     with open(fname, "a") as file:
#                     file.write(f"oval count  = {c_count}   textbox count  = {t_count} \n ")

#     doc.close()
# ---------------------------------------------------------------    

#--------------------- to count the similar color of oval and textboxes--------------------------
def ov_tb_counter(fname):
    # print(f"  oval {o_list}")
    # print(f" textbox {t_list}") 
    # global o_list
    # global t_list

    o = o_list                                                             # assigining the oval list to o
    t = t_list                                                            # assigining the textbox list to t
    print(f"o list {o}")
    print(f"tb list {t}")
    oval_count={}                                                         # to store the the oval rgb value and the count as dictionary
    tb_count={}                                                           # to store the the textbox rgb value and the count as dictionary

    for my_tuple in o: # to count the oval and assign it to dictionary
        if my_tuple in oval_count:                                       # if the rgb tuple is present increment the count
            oval_count[my_tuple] += 1
        else:                                                            # if the rgb tuple is not present in dictionary add the rgb tuple to dictionary
            oval_count[my_tuple] = 1

# Print the distinct tuples and their counts
    # for my_tuple, count in oval_count.items():
    #     print(f"Tuple {my_tuple} appears {count} times.")
    for my_tuple in t: # to count the tb and assign it to dictionary
        if my_tuple in tb_count:                                        # if the rgb tuple is present increment the count
            tb_count[my_tuple] += 1
        else:                                                           # if the rgb tuple is not present in dictionary add the rgb tuple to dictionary
            tb_count[my_tuple] = 1


    with open(fname, "a") as file:
        # file.write(f"oval count  = {c_count}   textbox count  = {t_count} \n ")
        for my_tuple, count in oval_count.items():                        # To access the oval dictionary
            #file.write(f"oval color {my_tuple} appears {count} times.\n")
            try:                                                        # to check if the rbg color has name
                clr =  wb.rgb_to_name(my_tuple)                         # converitng to rgb color name
                file.write(f"Oval {clr} appears {count} times.\n")         # writing to file
            except ValueError:                                            # executed when the color name is not present of the rgb
                 file.write(f"Oval {my_tuple} appears {count} times.\n ")
        for my_tuple, count in tb_count.items():
            try:
                clr =  wb.rgb_to_name(my_tuple)
                file.write(f"Textbox {clr} appears {count} times.\n")
            except ValueError:
                 file.write(f"Textbox {my_tuple} appears {count} times.\n ")
                 
            


pdf_path = 'C:/Users/user105/Documents/pandas_learning/sample.pdf'

fname = os.path.basename(pdf_path)      #  to get the name of pdf file
print(fname)

fname = fname.replace('.pdf', '.txt')        # replacing .pdf extension to .txt to make it as a txt file
print(fname)

print_count(pdf_path,fname)
ov_tb_counter(fname)

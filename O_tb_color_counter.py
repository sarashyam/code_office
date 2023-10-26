import fitz
import os
import webcolors as wb

class myexp(Exception):
    def __init__(self, message="color not found"):
        super().__init__(message)

c_count = 0
t_count = 0
o_list =[]
t_list =[]

def print_count(pdf_path,fname):
    global c_count
    global t_count
    global o_list 
    global t_list

    doc = fitz.open(pdf_path)
    c = (5, 'Circle')
    t = (2, 'FreeText', 'FreeText')

    for page_num in range(len(doc)):
        page = doc[page_num]
        for annotation in page.annots():
            typ = annotation.type

            if "Circle" in typ:     # typ == c:
                c_count+=1
                clr = annotation.colors # to get the annotation color
                        #print(clr)
                val = clr['fill']
                #o_list.append(val)
                #print(val)
                if val != None:
                            rgb_normalized = clr['fill']
                            rgb_original = tuple(int(round(component * 255, 1)) for component in rgb_normalized)
                            #print(f"rgb converted {rgb_original} value ")
                            o_list.append(rgb_original)
                             


            if 2 in typ:            #typ == t:
                t_count+=1
                clr = annotation.colors # to get the annotation color
                        #print(clr)
                val = clr['stroke']
                #o_list.append(val)
                #print(val)
                if val != None:
                            rgb_normalized = clr['stroke']
                            rgb_original = tuple(int(round(component * 255, 1)) for component in rgb_normalized)
                            #print(f"rgb converted {rgb_original} value ")
                            t_list.append(rgb_original)



    with open(fname, "a") as file:
                    file.write(f"oval count  = {c_count}   textbox count  = {t_count} \n ")

    doc.close()
    # print(f"  oval {o_list}")
    # print(f" textbox  {t_list}")




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
    

def ov_tb_counter(fname):
    # print(f"  oval {o_list}")
    # print(f" textbox {t_list}") 
    # global o_list
    # global t_list

    o = o_list
    t = t_list
    print(f"o list {o}")
    print(f"tb list {t}")
    oval_count={}
    tb_count={}

    for my_tuple in o:
        if my_tuple in oval_count:
            oval_count[my_tuple] += 1
        else:
            oval_count[my_tuple] = 1

# Print the distinct tuples and their counts
    # for my_tuple, count in oval_count.items():
    #     print(f"Tuple {my_tuple} appears {count} times.")
    for my_tuple in t:
        if my_tuple in tb_count:
            tb_count[my_tuple] += 1
        else:
            tb_count[my_tuple] = 1


    with open(fname, "a") as file:
        # file.write(f"oval count  = {c_count}   textbox count  = {t_count} \n ")
        for my_tuple, count in oval_count.items():
            #file.write(f"oval color {my_tuple} appears {count} times.\n")
            try:
                clr =  wb.rgb_to_name(my_tuple)
                file.write(f"Oval {clr} appears {count} times.\n")
            except ValueError:
                 file.write(f"Oval {my_tuple} appears {count} times.\n ")
        for my_tuple, count in tb_count.items():
            try:
                clr =  wb.rgb_to_name(my_tuple)
                file.write(f"Textbox {clr} appears {count} times.\n")
            except ValueError:
                 file.write(f"Textbox {my_tuple} appears {count} times.\n ")
                 
            


pdf_path = 'C:/Users/user105/Documents/pandas_learning/sample.pdf'

fname = os.path.basename(pdf_path)
print(fname)

fname = fname.replace('.pdf', '.txt')
print(fname)

print_count(pdf_path,fname)
ov_tb_counter(fname)
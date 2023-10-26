import fitz
import os
# def is_oval(annotation):
    # print(annotation.type)
    # # Check if the annotation is an oval (ellipse)
    # return annotation.type == 5  # Type 5 corresponds to an ellipse annotation
def print_count(pdf_path,fname):
    c_count = 0
    t_count = 0

    doc = fitz.open(pdf_path)
    c = (5, 'Circle')
    t = (2, 'FreeText', 'FreeText')

    for page_num in range(len(doc)):
        page = doc[page_num]
        for annotation in page.annots():
            typ = annotation.type
<<<<<<< HEAD
=======
            #print(annotation.colors)
            # print(annotation.rect)   to print the x0 yo x1 y1 coordinates where it is located
            print(annotation.rect.y1) # to print y1 coordinates
            #print(annotation.author)
            

>>>>>>> 0952743799ed21bc060ee215418d02d0e7200d39

            if "Circle" in typ:     # typ == c: to check if circle 5 is present in annotation type tuple
                c_count+=1

            if 2 in typ:            #typ == t:  to check if freetext 2 is present in annotation type tuple
                t_count+=1

    with open(fname, "a") as file:
                    file.write(f"oval count  = {c_count}   textbox count  = {t_count} \n ")

    doc.close()

def extract_oval_annotations(pdf_path,fname):

        c_count = 0
        t_count = 0
        oc_count = 0
        # oval_annotations = []
        doc = fitz.open(pdf_path)
        print(doc)
        c = (5, 'Circle')
        t = (2, 'FreeText', 'FreeText')

        a_type = int(input("enter the type to find ,  for textbox enter 2  for oval enter 5 "))

        input_str = input("Enter rgb values separated by commas: ") # r=

                    # Split the input string by commas, convert to integers, and create a tuple
        integer_list = input_str.split(',')
        integer_tuple = tuple(int(x) for x in integer_list)
        print(f" the integer tuple is {integer_tuple}")

        oval_set=[]
        text_set={}


        for page_num in range(len(doc)):
            page = doc[page_num]
            for annotation in page.annots():
                #print(annotation.type)
                print(annotation)
                typ = annotation.type
                #print(annotation.colors)
                #print(annotation.rect.y1)
                #print(annotation.author)
                


                if 5 in typ  and a_type == 5:     # typ == c:
                    c_count+=1
                    
                    
                    
                    with open(fname, "a") as file:
                        
                        clr = annotation.colors # to get the annotation color
                        #print(clr)
                        val = clr['fill']
                        oval_set.append(val)
                        print(val)
                        if val != None:
                            rgb_normalized = clr['fill']
                            rgb_original = tuple(int(round(component * 255, 1)) for component in rgb_normalized)
                            print(f"rgb converted {rgb_original} value ")
                            if(integer_tuple == rgb_original):
                                oc_count+=1
                                print(f"oval of  {integer_tuple} color has been found {oc_count}")

                        #print(annotation.colors)
                        #file.write(f"location of  oval no {c_count} is\n xo yo x1 y1 {annotation.rect}\n")
                        # print(" added")
                        
                    #print(f"Oval annotation found on page {annotation.page_number} at ({annotation.x}, {annotation.y})")

                if 2 in typ and a_type == 2:            #typ == t:
                    t_count+=1
                    with open(fname, "a") as file:
                        
                        clr = annotation.colors # to get the annotation color
                        # print(clr)
                        val = clr['stroke']
                        print(val)
                        if val != None:
                        #print(clr)y

                            rgb_normalized = clr['stroke']
                            rgb_original = tuple(int(round(component * 255, 1)) for component in rgb_normalized)
                            print(f"rgb converted {rgb_original} value ")
                            if(integer_tuple == rgb_original):
                                oc_count+=1
                                print(f"textbox of  {integer_tuple} color has been found {oc_count}")
                        
                        #file.write(f"location of  textbox no {t_count} is\n xo yo x1 y1 {annotation.rect}\n")
                        
                


                # if annotation.subtype == '/Circle':
                #     print("I'm a circle")
                #     c_count+=1

                # if annotation.type == t:
                #     t_count+=1
                # if is_oval(annotation):
                #     oval_annotations.append(annotation)
        
        # fname = os.path.basename(pdf_path)
        

        # print(fname)

        # fname = fname.replace('.pdf', '.txt')
        # print(fname)
        #-----------------
        # print(f"oval count {c_count} and textbox count {t_count}")
        with open(fname, "a") as file:
                        # file.write(f"oval count  = {c_count}   textbox count  = {t_count} \n ")
                        if a_type == 5:
                            file.write(f"no of oval of {integer_tuple} color = {oc_count}\n ")
                        if a_type == 2:
                            file.write(f"no of textbox of {integer_tuple} color = {oc_count}\n ")
                              
        #---------------------

        doc.close()
        

    
   
    #return oval_annotations

# Usage example
<<<<<<< HEAD
pdf_path = 'C:/Users/user105/Documents/pandas_learning/sample.pdf'

fname = os.path.basename(pdf_path)
print(fname)

fname = fname.replace('.pdf', '.txt')
print(fname)
# print(f"oval count {c_count} and textbox count {t_count}")
# with open(fname, "a") as file:
#         file.write(f"oval count {c_count} and textbox count {t_count}")


print_count(pdf_path,fname)
while True:
    choice = input("do you want to find count of oval or textbox based on color , if yes enter 1 , if no press any key")
    if choice == 'y':
        oval_annotations = extract_oval_annotations(pdf_path,fname)
    else:
          exit()
=======
pdf_path = 'C:/Users/user105/Documents/pandas_learning/find_textboxes.pdf' # path of the pdf file
oval_annotations = extract_oval_annotations(pdf_path)
>>>>>>> 0952743799ed21bc060ee215418d02d0e7200d39

# for annotation in oval_annotations:
#     # Handle oval annotations as needed
#     print(f"Oval annotation found on page {annotation.page_number} at ({annotation.x}, {annotation.y})")

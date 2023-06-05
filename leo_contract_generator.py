neurons_per_layer = [8,4,4, 6] # specifies NN architecture
integer_type = "i64" # specifies used integer type

if(len(neurons_per_layer) < 2 or min(neurons_per_layer) < 1):
   print("error, invalid input")

str_list_main = []
str_list_inputs = []

#1. add program neural_network.aleo
str_program="program neural_network.aleo{\n"
str_list_main.append(str_program)


seen_strings = set()
dict = {}
dict_list = []
dict_list_S = []
dict_P = {}
max = 0; 
emb_input = []
count_weight = 0
for layer in range(1, len(neurons_per_layer)): # other layers
   count = 0
   emb_count = 1
   index = 1 
   str_struct = [] 
   list_all = []
   emb_struct =[]
   emb_all_struct = []
   emb_index = 1
   for i in range(neurons_per_layer[layer]):
       for j in range(neurons_per_layer[layer-1]):
           count += 1 
           count_weight += 1
           if str(layer) + str(j) + str(i) in seen_strings:
               str_struct.append("w" + str(layer) + str(j) + str(i) + "w" + ": " + integer_type + ",")
               dict_list.append("w" + str(layer) + str(j) + str(i) + "w")
           else: 
               str_struct.append("w" + str(layer) + str(j) + str(i) + ": " + integer_type + ",")
               dict_list.append("w" + str(layer) + str(j) + str(i))
           seen_strings.add(str(layer) + str(j) + str(i))    
           if count%32 == 0:
               # dict_list_S.append("s" + str(layer) + str(index))
               struct =  "struct S" + str(layer) + str(index) +  "{\n" + " ".join(str_struct) + "\n}\n"
               str_list_main.append(struct)
               for key in dict_list:
                  dict[key] = "s" + str(layer) + str(index)
               dict_list.clear()
               emb_struct.append("s" + str(layer) + str(index) + ": " + "S" + str(layer) + str(index) + ",")
               # for key in dict_list_S:
               key_p = "s" + str(layer) + str(index)
               dict_P[key_p] = "p" + str(layer) + str(emb_index)
               if emb_count%32 == 0:
                  dict_list_S.clear()
                  P = "struct P" + str(layer) + str(emb_index) + "{\n" + " ".join(emb_struct) + "\n}\n"
                  pinput =  "p"+ str(layer) + str(emb_index) + ":" + "P" + str(layer) + str(emb_index)
                  emb_input.append(pinput)
                  emb_all_struct.append(P)
                  emb_index += 1 
                  emb_struct = []
               index += 1
               emb_count += 1 
               str_struct = []
           elif count == neurons_per_layer[layer]*neurons_per_layer[layer-1]:
              key_p = "s" + str(layer) + str(index)
              dict_P[key_p] = "p" + str(layer) + str(emb_index)
              struct =  "struct S" + str(layer) + str(index) +  "{\n" + " ".join(str_struct) + "\n}\n"
              str_list_main.append(struct)
              for key in dict_list:
                  dict[key] = "s" + str(layer) + str(index)
              dict_list.clear()
              emb_struct.append("s" + str(layer) + str(index) + ": " + "S" + str(layer) + str(index) + ",")
   if len(emb_struct) >0 and len(emb_struct) <= 32:
      P = "struct P" + str(layer) + str(emb_index) + "{\n" + " ".join(emb_struct) + "\n}\n"
      pinput =  "p"+ str(layer) + str(emb_index) + ":" + "P" + str(layer) + str(emb_index)
      emb_input.append(pinput)
      emb_all_struct.append(P)   
   for p in emb_all_struct:
      str_list_main.append(p)  
      
   
seen_strings.clear()


index = len(neurons_per_layer)
str_struct="struct S"
str_struct += str(index) + "{\n"
for i in range(neurons_per_layer[0]):
   str_struct += "input" + str(i) + ": " + integer_type + ","
   if i!=0 and i % 31 == 0:
      str_struct += "\n}\n"
      str_list_main.append(str_struct)  
      str_struct="struct S"
      str_struct += str(index+1) + "{\n" 
str_struct += "\n}\n"
str_list_main.append(str_struct)


b_list = []
b_dict = {}
str_struct1 = []
index = 0
b_index = 1 
count = 0
B_list = []
b_count = 0 
for i in range(1, len(neurons_per_layer)): 
   for j in range(0,neurons_per_layer[i]): 
      b_count += 1 
for i in range(1, len(neurons_per_layer)): # current layer
   for j in range(0,neurons_per_layer[i]): # neuron of previous layer
      str_struct1.append("b" + str(i) + str(j) + ": " + integer_type + ",")
      count += 1
      key = "b" + str(i) + str(j)
      b_list.append(key)
      if len(b_list)%32 == 0:
         for key in b_list:
            b_dict[key] = "b" + str(index+1)
         b_list.clear()
         index += 1 
      if count%32 == 0:
         emb_b =  "b" + str(index)+": " + "B" + str(index) + ", "
         B_list.append(emb_b)
         struct =  "struct B" + str(index) +  "{\n" + " ".join(str_struct1) + "\n}\n"
         str_list_main.append(struct)
         str_struct1.clear()
      elif count == b_count:
         for key in b_list:
            b_dict[key] = "b" + str(index+1)
         b_list.clear()
         emb_b =  "b" + str(index+1)+": " + "B" + str(index+1) + ", "
         B_list.append(emb_b)
         struct =  "struct B" + str(index+1) +  "{\n" + " ".join(str_struct1) + "\n}\n"
         str_list_main.append(struct)
         str_struct1.clear()

B_struct = "struct B{\n" + " ".join(B_list) + "\n}\n"
str_list_main.append(B_struct)

Return_struct = "struct Res{\n"
for i in range(0,neurons_per_layer[-1]):
   Return_struct += " " + "r" + str(i) + ": " +  integer_type + ","


Return_struct += "\n}\n"

str_list_main.append(Return_struct)
str_main="transition main("

str_inputs = ""

str_list_inputs.append("[main]\n")

for i in range(neurons_per_layer[0]):
   #str_main += "w0" + str(i)+": " + integer_type + ", b0" + str(i) + ": " + integer_type + ", "
   #str_inputs += "w0" + str(i) + ": " + integer_type + " = 0;\n"
   #str_inputs += "b0" + str(i) + ": " + integer_type + " = 0;\n"
   pass

str_list_inputs.append(str_inputs)
str_inputs = ""

for i in range(1, len(neurons_per_layer)): # current layer
   for j in range(neurons_per_layer[i-1]): # neuron of previous layer
       for k in range(neurons_per_layer[i]): # neuron of current layer
           str_inputs += "w" + str(i) + str(j) + str(k) + ": " + integer_type + " = 0;\n"
       str_inputs +=  "b" + str(i) + str(j) + ": " + integer_type + " = 0;\n"
      
for i in range(neurons_per_layer[0]):
   str_inputs +=  "input"+str(i)+": " + integer_type + " = 0;\n"


str_list_inputs.append(str_inputs)

str_inputs = "[registers]\n"


for input in emb_input:
   str_main += input + ","

num = int(neurons_per_layer[0]/32) + 1 
for i in range(0,num):
   str_main += "s" + str(len(neurons_per_layer)+i)+ ":" + "S" + str(len(neurons_per_layer)+i) + ","
str_main += "b:B" + ","


str_main = str_main[:-1]
str_main += ") ->"+"Res" + "{\n"
str_list_main.append(str_main)

line = ""

for i in range(neurons_per_layer[0]): # input layer
   if i <= 31:
      line += "let neuron0"+str(i) + ": " + integer_type + " = " + "s" + str(len(neurons_per_layer)) + "." + "input" + str(i)  + ";\n"
   else:
      line += "let neuron0"+str(i) + ": " + integer_type + " = " + "s" + str(len(neurons_per_layer)+1) + "." + "input" + str(i)  + ";\n"

for layer in range(1, len(neurons_per_layer)): # other layers
   for i in range(neurons_per_layer[layer]):
       activation_function_start = "rectified_linear_activation("
       activation_function_end = ")"
       if layer == len(neurons_per_layer)-1:
          activation_function_start = "" 
          activation_function_end = ""
       line_start = "let neuron" + str(layer) + str(i) + ": " + integer_type + " = " + activation_function_start
       for j in range(neurons_per_layer[layer-1]):
            if str(layer) + str(j) + str(i) in seen_strings:
               key = "w" + str(layer) + str(j) + str(i) + "w"
               s = dict[key]
               p = dict_P[s]
               if layer -1 == 0:
                  line_start += "neuron" + str(layer-1) + str(j) + " * " + p + "." + s + "." + key   + " / " + str(1000000) + integer_type + " " + " + " 
               else:
                  line_start += "neuron" + str(layer-1) + str(j) + " * " + p + "." + s + "." + key   + " / " + str(1000000) + integer_type + " " + " + " 
            else:   
              key = "w" + str(layer) + str(j) + str(i) 
              s = dict[key]
              p = dict_P[s]
              if layer -1 == 0:
                  line_start += "neuron" + str(layer-1) + str(j) + " * " + p + "." + s + "." + key    + " / " + str(1000000) + integer_type + " " + " + " 
              else:
                  line_start += "neuron" + str(layer-1) + str(j) + " * " + p + "." + s + "." + key    + " / " + str(1000000) + integer_type + " " + " + "
            seen_strings.add(str(layer) + str(j) + str(i))
       key = "b" + str(layer) + str(i)
       b = b_dict[key]
       line_start +=  "b" + "." + b + "." + "b" + str(layer) + str(i) +  activation_function_end + ";\n"
       line += line_start
      
str_list_main.append(line)



str_inputs += "r0: [" + integer_type + "; " + str(neurons_per_layer[-1]) + "] = ["
for i in range(neurons_per_layer[-1]):
   str_inputs += "0, "
str_inputs = str_inputs[:-2] + "];\n"

layer = len(neurons_per_layer)-1
line = "let res:Res = Res{\n"
for i in range(0,neurons_per_layer[-1]):
    line +=  " " +  "r" + str(i) + ":" + "neuron" + str(layer) + str(i) + ","

line += "\n};\n " + "return res;\n}\n"
# line += ";\n}\n\n"
str_list_main.append(line)
str_list_inputs.append(str_inputs)

str_list_main.append("function rectified_linear_activation(x: i64) -> i64 {\n")
str_list_main.append("let result: i64 = 0i64;\n")
str_list_main.append("if x > 0i64 {\n")
str_list_main.append("result = x;\n")
str_list_main.append("}\n")
str_list_main.append("return result;\n")
str_list_main.append("}\n")
str_list_main.append("}")
with open("main.leo", "w+") as file:
   file.writelines(str_list_main)

with open("project.in", "w+") as file:
   file.writelines(str_list_inputs)

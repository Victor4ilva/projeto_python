

while True:
   a=int(input("Digite um valor: "))
   b=int(input("Digite outro valor: "))
   print("Escolha uma opção:")
   print("   SOMAR    (1)")
   print("  SUBTRAIR  (2)")
   print("MULTIPLICAR (3)")
   print("  DIVIDIR   (4)")
   print("   SAIR     (0)")
   
   opcao=int(input(":"))
   if opcao == 0:
       break
   elif opcao == 1:
       resultado=a*b
       print(f"{a}+{b}= {a+b}")
    
       
   elif opcao == 2:
       resultado=a-b
       print(f"{a}-{b}= {a-b}")
       
   elif opcao == 3:
       resultado=a*b
       print(f"{a}x{b}= {a*b}")
       
   elif opcao == 4:
       resultado=a/b
       print(f"{a}/{b}= {a/b}")
       
  
    
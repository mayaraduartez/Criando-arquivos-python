nomes = ["Mayara","Amanda", "Diulli", ""]


#percorre a lista escrevendo um por um
with open("teste2.txt", "w") as writer:
    for nome in nomes:
        writer.write(nome+ "\n")
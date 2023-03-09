# initialize the menu variables
rice = [""]
beans = [""]
meats = [""]
sides = [""]
salads = ["\n🥬Alface", "🍅Tomate", "🥬Rúcula", "🍅Vinagrete", "🍍Abacaxi", "🥭Manga", "🥕Cenoura", "🍠Beterraba", "🥒Pepino"]
sections = {"rice": rice, "beans": beans, "meats": meats, "sides": sides, "salads": salads}

emoji_map = {
    "Arroz": "🍚",
    "Arroz Integral": "🍚",
    "Arroz de Forno": "🍚",
    "Arroz Temperado": "🍚",
    "Galinhada": "🐓",
    #########################



    "Feijão": "🥘",
    "Feijão Preto": "🥘",
    "Feijão Tropeiro": "🥘",
    "Feijão Branco": "🥘",
    "Feijoada": "🥘",
    "Tutu de Feijão": "🥘",
    #########################



    "Bife Acebolado": "🥩",
    "Carne Moída com Legumes": "🥩",
    "Carne Moída": "🥩",
    "Hambúrguer à Pizzaiolo": "🥩",
    "Ponta de Peito": "🥩",
    "Ponta de Peito ao Alho": "🥩",
    "Carne Bovina Assada": "🥩",
    "Carne Bovina Grelhada": "🥩",
    "Carne Bovina ao Molho": "🥩",
    "Almôndegas Fritas": "🥩",
    "Almôndegas ao Molho": "🥩",
    "Rabada": "🥩",
    "Strogonoff Bovino": "🥩",
    "Tiras de Costela": "🥩",
    "Ripa de Costela": "🥩",
    "Bife de Panela": "🥩",
    "Carne de Panela": "🥩",
    "Picadinho Bovino": "🥩",
    "Picadinho Bovino ao Molho": "🥩",
    "Picadinho Bovino ao Molho Madeira": "🥩",
    "Iscas Bovinas": "🥩",
    #########################

    "Frango Grelhado": "🐓",
    "Frango Frito": "🐓",
    "Frango Assado": "🐓",
    "Frango ao Molho": "🐓",
    "Frango Caipira": "🐓",
    "Strogonoff de Frango": "🐓",
    "Frango à Passarinho": "🐓",
    "Frango Empanado": "🐓",
    "Picadinho de Frango": "🐓",
    "Pipoca de Frango Empanado": "🐓",
    "Iscas de Frango Empanadas": "🐓",
    #########################

    "Carne Suína Assada": "🍖",
    "Carne Suína Grelhada": "🍖",
    "Carne Suína ao Molho": "🍖",
    "Lombo Grelhado": "🍖",
    "Lombo Assado": "🍖",
    "Lombo ao Molho": "🍖",
    "Lombo ao Molho de Alho": "🍖",
    "Bife Suíno": "🍖",
    "Bife Suíno Acebolado": "🍖",
    "Pernil Assado": "🍖",
    "Pernil de Panela": "🍖",
    "Picadinho Suíno": "🍖",
    "Picadinho Suíno ao Molho Madeira": "🍖",
    #########################



    "Batata Frita": "🍟",
    "Batata Assada": "🥔",
    "Batata ao Molho": "🥔",
    "Batata Rústica": "🥔",
    "Batata com Ervas": "🥔",
    "Batata Gratinada": "🥔",
    "Batata Chips": "🥔",
    #########################

    "Batata Doce": "🍠",
    "Batata Doce Frita": "🍠",
    "Batata Doce Chips": "🍠",
    "Batata Doce Cozida": "🍠",
    #########################

    "Couve Refogada": "🥦",
    "Couve com Bacon": "🥦",
    "Abobrinha Refogada": "🥦",
    "Espaguete de Abobrinha": "🥦",
    "Virado de Abobrinha": "🥦",
    "Abobrinha ao Molho": "🥦",
    "Quiabo Refogado": "🥦",
    "Quiabo Frito": "🥦",
    "Chuchu Refogado": "🥦",
    "Mix de Legumes": "🥦",
    "Legumes na Manteiga": "🥦",
    "Jiló Frito": "🥦",
    "Jiló Refogado": "🥦",
    "Virado de Jiló": "🥦",
    "Couve-flor Refogada": "🥦",
    "Couve-flor Gratinada": "🥦",
    "Couve-flor Empanada": "🥦",
    "Brócolis Refogado": "🥦",
    "Repolho Refogado": "🥦",
    "Vagem Refogada": "🥦",
    #########################
    
    "Berinjela Refogada": "🍆",
    "Berinjela da Casa": "🍆",
    "Berinjela Frita": "🍆",
    "Berinjela à Parmegiana": "🍆",
    "Berinjela à Parmegiana(sem Presunto)": "🍆",
    #########################

    "Banana Frita": "🍌",
    "Banana Empanada": "🍌",
    "Farofa de Banana": "🍌",
    "Banana Flambada": "🍌",
    #########################

    "Nhoque": "🥔",
    "Nhoque ao Sugo": "🥔",
    "Nhoque ao Molho Rosé": "🥔",
    "Nhoque ao Molho": "🥔",
    #########################

    "Macarrão": "🍝",
    "Macarrão Alho e Óleo": "🍝",
    "Macarrão de Forno": "🍝",
    "Macarrão ao Molho Rosé": "🍝",
    "Macarrão com Brócolis": "🍝",
    "Macarrão com Brócolis e Bacon": "🍝",
    "Macarrão ao Sugo": "🍝",
    #########################

    "Ovos Fritos": "🍳",
    "Omelete": "🍳",
    "Omelete de Forno": "🍳",
    "Omelete Recheado": "🍳",
    #########################

    "Cenoura Refogada": "🥕",
    "Cenoura Cozida": "🥕",
    "Cenoura com Bacon": "🥕",
    "Cenoura com Calabresa": "🥕",
    #########################

    "Pastel de Presunto e Muçarela": "🍖",
    "Pastel de Carne": "🍖",
    "Pastel de Calabresa": "🍖",
    "Rondelli de Presunto e Muçarela": "🍖",
    "Rondelli de Carne": "🍖",
    "Canelone de Presunto e Muçarela": "🍖",
    "Canelone de Carne": "🍖",
    "Lasanha de Presunto e Muçarela": "🍖",
    "Lasanha de Carne": "🍖",
    #########################

    "Milho Refogado": "🌽",
    "Creme de Milho": "🌽",
    "Milho Cozido": "🌽",
    "Milho na Espiga": "🌽",
    #########################

    "Escondidinho de Frango": "🐓",
    #########################


    "Maionese": "🥗",
    "Tabule": "🥗",
    "Salpicão": "🥗",
    "Dakota": "🥗",
    "Batatonese": "🥗",
    "Batata Verde": "🥗",
    "Batata Temperada": "🥗",
    "Salada Caprese": "🥗",
    "Repolhonese": "🥗",
    #########################
}

# take input from the user for each dish and add it to the appropriate list
for section_name, section in sections.items():
    while True:
        dish = input(f"Enter a dish for {section_name} or 'next' to proceed: ")
        if dish == "next": 
            break
        else:
            emoji = emoji_map.get(dish, "😋") # use the corresponding emoji, or a default one if not found
            section.append(f"{emoji}{dish}")

# print the menu 
print("Bom dia!\n\nSegue o cardápio para marmitex e marmita:")

print("\n".join(rice))
print("\n".join(beans))
print("\n".join(meats))
print("\n".join(sides))
print("\n".join(salads))

print("\n\n📃Cardápio sujeito a alteração ao longo do expediente.\n📝 Para realizar seu pedido, mande a mensagem no privado da conta do Restaurante Cozinha & Cia.\n👨‍🍳Nosso tempero é nosso toque!\n🍝Self service | Marmitex | Marmita \n📍Seg. à Sex. - 10h45 às 14h - Sáb. - 10h45 às 14h30\n📞3403-7869\n📞98141-4737 \n❤Amamos a Cozinha & a Sua CIA")

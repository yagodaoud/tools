# initialize the menu variables
rice = [""]
beans = [""]
meats = [""]
sides = [""]
salads = ["\n🥬Alface", "🍅Tomate", "🥬Rúcula", "🍅Vinagrete", "🍍Abacaxi", "🥭Manga", "🥕Cenoura", "🍠Beterraba", "🥒Pepino"]
sections = [rice, beans, meats, sides, salads]

# take input from the user for each dish and add it to the appropriate list
for section in sections:
    while True:
        dish = input("Enter a dish for a section or 'next' to proceed: ")
        if dish == "next": 
            break
        else:
            section.append("🍚" + dish if section is rice else "🥘" + dish if section is beans else "🥩" + dish if section is meats else "😋" + dish if section is sides else "🥬" + dish)

# print the menu in the same format as the WhatsApp message
print("Bom dia!\nSegue o cardápio para marmitex e marmita:")

print("\n".join(rice))
print("\n".join(beans))
print("\n".join(meats))
print("\n".join(sides))
print("\n".join(salads))

print("📃Cardápio sujeito a alteração ao longo do expediente.\n📝 Para realizar seu pedido, mande a mensagem no privado da conta do Restaurante Cozinha & Cia.\n👨‍🍳Nosso tempero é nosso toque!\n🍝Self service | Marmitex | Marmita \n📍Seg. à Sex. - 10h45 às 14h - Sáb. - 10h45 às 14h30\n📞3403-7869\n📞98141-4737 \n❤Amamos a Cozinha & a Sua CIA")
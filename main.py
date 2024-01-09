contacts = []


def showMenu():
    print("\nLista de Contatos:")
    print("1 - Adicionar um novo contato"),
    print("2 - Listar todos os contatos"),
    print("3 - Listar os contatos favoritos"),
    print("4 - Adicionar um contato aos favoritos"),
    print("5 - Remove um contato dos favoritos"),
    print("6 - Editar um contato"),
    print("7 - Remover um contato"),
    print("8 - Sair")


def addNewContact():
    name = input("Nome do contato: ")
    phone = input("Telefone do contato: ")
    email = input("Email do contato: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "favorite": False
    })
    print("Contato adicionado com sucesso")


def listAllContacts():
    print("\nLista de contatos:")
    for i, c in enumerate(contacts, start=1):
        favorite_status = "Favorito" if c["favorite"] else "Não favorito"
        name, email, phone = c["name"], c["email"], c["phone"]

        print(f"  {i} - {name}; {email}; {phone} - {favorite_status}")


def listFavoriteContacts():
    print("\nLista de contatos favoritos:")
    favorite_contacts = [c for c in contacts if c["favorite"]]

    for i, c in enumerate(favorite_contacts, start=1):
        name, email, phone = c["name"], c["email"], c["phone"]

        print(f"  {i} - {name}; {email}; {phone}")

    return favorite_contacts


def addContactAsFavorite():
    listAllContacts()

    contact_selected = int(input("Qual o contato deseja favoritar: "))

    if contact_selected < 1 or contact_selected > len(contacts):
        return

    contact_selected -= 1

    contacts[contact_selected]["favorite"] = True


def removeContactAsFavorite():
    favorite_contacts = listFavoriteContacts()

    contact_selected = int(input("Qual o contato deseja desfavoritar: "))

    if contact_selected < 1 or contact_selected > len(favorite_contacts):
        return

    contact_selected -= 1

    favorite_contacts[contact_selected]["favorite"] = False


def editContact():
    listAllContacts()

    contact_selected = int(input("Qual o contato deseja remover: "))

    if contact_selected < 1 or contact_selected > len(contacts):
        return

    contact_selected -= 1

    name = input("Digite um novo nome (deixe vazio para manter): ")
    phone = input("Digite um novo telefone (deixe vazio para manter): ")
    email = input("Digite um novo email (deixe vazio para manter): ")

    if len(name) > 0:
        contacts[contact_selected]["name"] = name

    if len(phone) > 0:
        contacts[contact_selected]["phone"] = phone

    if len(email) > 0:
        contacts[contact_selected]["email"] = email


def removeContact():
    listAllContacts()

    contact_selected = int(input("Qual o contato deseja remover: "))

    if contact_selected < 1 or contact_selected > len(contacts):
        return

    contact_selected -= 1

    del contacts[contact_selected]


def execute():
    while True:
        try:
            showMenu()

            choice = int(input("Digite o número de sua escolha: "))

            match choice:
                case 1: addNewContact()
                case 2: listAllContacts()
                case 3: listFavoriteContacts()
                case 4: addContactAsFavorite()
                case 5: removeContactAsFavorite()
                case 6: editContact()
                case 7: removeContact()
                case 8: break
                case _: print("Opção de menu inválida")

        except KeyboardInterrupt:
            break
        except ValueError:
            print("Digite apenas números")


if __name__ == "__main__":
    execute()

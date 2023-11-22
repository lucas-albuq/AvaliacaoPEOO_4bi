import json

class Cliente:

    def __init__(self, id, nome, email, fone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_fone(self):
        return self.__fone

    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def set_fone(self, fone):
        self.__fone = fone

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
    
    def __eq__(self, x):
        if self.__id == x.__id and self.__nome == x.__nome and self.__email == x.__email and self.__fone == x.__fone:
            return True
        return False
    
class NCliente:
    __clientes = []
    
    @classmethod
    def inserir(cls, obj):
        NCliente.abrir()
        id = 0
        for cliente in cls.__clientes:
            if cliente.get_id() > id: id = cliente.get_id()
        obj.set_id(id+1)
        cls.__clientes.append(obj)
        NCliente.salvar()

    @classmethod
    def listar(cls):
        NCliente.abrir()
        return cls.__clientes

    @classmethod
    def listar_id(cls, id):
        NCliente.abrir()
        for obj in cls.__clientes:
            if obj.get_id() == id:
                return obj
        return None    

    @classmethod
    def atualizar(cls, obj):
        NCliente.abrir()
        c = NCliente.listar_id(obj.get_id())
        if c is not None:
            c.set_nome(obj.get_nome)
            c.set_email(obj.get_email)
            c.set_fone(obj.get_fone)
            NCliente.salvar()

    @classmethod
    def excluir(cls, obj):
        NCliente.abrir()
        c = NCliente.listar_id(obj.get_id())
        if c is not None:
            cls.__clientes.remove(c)
            NCliente.salvar()

    @classmethod
    def abrir(cls):
        try:
            cls.__clientes = []
            with open("Clientes.json", "r") as f:
                clientes_json = json.load(f)
                for obj in clientes_json:
                    c = Cliente(obj["_Cliente__id"], obj["_Cliente__nome"], obj["_Cliente__email"], obj["_Cliente__fone"])
                    cls.__clientes.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('Clientes.json', 'w') as f:
            json.dump(cls.__clientes, f, default=vars)
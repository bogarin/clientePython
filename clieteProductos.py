import suds

class Client:
    #conocido como constructor establese la conexion
    def __init__(self):
        self.client = suds.client.Client("http://localhost:8181/WS/Mercado?wsdl")

    def categorias(self, categoria):
        resultado_categorias = self.client.service.getProduct(categoria)
        for l in resultado_categorias:
            print '%s' %(l)

    def gregarProducto(self):
        categoria = raw_input('Escribe la categoria ')
        producto = raw_input('Escribe el producto ')
        if(self.client.service.addProduct(categoria,producto)):
            client.categorias(categoria)
        else:
            print "no lo agrego"

    def cat(self):
        resultado_categorias = self.client.service.setCategoria()
        for l in resultado_categorias:
            print '%s' %(l)

#metodo main
if(__name__ == "__main__"):
    client = Client()
    client.cat()

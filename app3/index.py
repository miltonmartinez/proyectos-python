from tkinter import ttk
from tkinter import *

import sqlite3
from datetime import datetime




class ConstruyeInterfaz:

    db_name = 'database.db'

    products = [('monitor',2450),('lentes',1450),('teclado',450),('monitor',2000),('raton',150),('CPU',20000),('pad',250),('cable',800),('RAM',1450),('SSD',700),('HDD',1450)]

    def __init__(self, window):
        self.wind = window
        self.wind.title('Product Aplicattion')          

        frame = LabelFrame(self.wind, text='Registra Nuevo Producto',bd=1, font=f"Arial 12")
        frame.grid(row=1,column=0, columnspan=2, pady=10)       

        Label(frame,text='Nombre: ').grid(row=2,column=0,padx=10, pady=10,sticky=E)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=2,column=1,padx=10, pady=10)

        Label(frame,text='Precio: $').grid(row=3,column=0,padx=10, pady=10,sticky=E)
        self.price = Entry(frame)
        self.price.grid(row=3,column=1,padx=10, pady=10)

        ttk.Button(frame, text='Guardar Producto', command=self.add_product).grid(row=4,columnspan=2,sticky=W+E,padx=10, pady=10)

        self.message = Label(text = '', fg = 'red')
        self.message.grid(row=4,column=3,columnspan=2,sticky=E, padx=10)

        self.total_registros = Label(text = '', fg = 'blue')
        self.total_registros.grid(row=4,column=0,columnspan=2,sticky=W, padx=10)

        self.tree = ttk.Treeview(height=10,columns=('',''))
        self.tree.grid(row=5,column=0,columnspan=5)
        
        self.tree.heading('#0', text='NOMBRE',anchor=W)
        self.tree.heading('#1', text='PRECIO',anchor=W)

        ttk.Button(text = 'BORRAR',command=self.delete_product).grid(row=6, column=0, sticky=W+E)
        ttk.Button(text = 'EDITAR',command=self.pre_edit_product).grid(row=6, column=1, sticky=W+E)
        ttk.Button(text = 'ACTUALIZAR',command=self.update_list).grid(row=6, column=2, sticky=W+E)
        ttk.Button(text = 'BORRAR TODO',command=self.delete_all).grid(row=6, column=3, sticky=W+E)
        ttk.Button(text = 'LLENAR',command=self.insert_all).grid(row=6, column=4, sticky=W+E)

        self.get_products()

    def insert_all(self):
        for product in self.products:
            query = 'insert into product values(null,?,?)'
            parameters = (product[0],product[1])
            self.run_query(query,parameters)
            self.get_products()
            self.message['text'] = 'Lista de Productos Actualizada'

    def update_list(self):
        self.get_products()
        self.message['text'] = 'Lista de Informacion Actualizada'

    def delete_all(self):
        query='delete from product'
        self.run_query(query)
        self.get_products()
        self.message['text'] = 'Todos los Registros Borrados'

    def run_query(self,query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            #print("Connected to SQLite")
            result = cursor.execute(query, parameters)
            #total = len(cursor.fetchall())
           # total = cursor.fetchmany()
            #print(len(r)) #print(r)
            conn.commit()
            info_result =result
            #print(rr)
        return (info_result,)

    def get_products(self):
        records =  self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = 'select id,name,price from product order by name desc'
        db_rows = self.run_query(query)[0]
        #self.total_registros['text'] = self.run_query(query)[1]
        #print(db_rows)
        count = 0
        for row in db_rows:
            #print(row[0])
            self.tree.insert('',0,open=row[0],text=str.upper(row[1]),values='$'+str(row[2]))
            count = count+1
        self.total_registros['text'] ="{} Productos".format(count)
            
    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0

    def add_product(self):
        if self.validation():
            query = 'insert into product values(null,?,?)'
            parameters = (self.name.get(),self.price.get())
            self.run_query(query,parameters)
            self.message['text'] = 'Producto {} Agregado'.format(self.name.get())
            self.name.delete(0,END)
            self.price.delete(0,END)
        else:
            self.message['text'] = 'Falta Nombre o Precio'
        self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
            id = self.tree.item(self.tree.selection())['open']            
            if id == 0:
                raise Exception()
        except:
            self.message['text'] = 'Selecciona Un Registro'
            return
        id = self.tree.item(self.tree.selection())['open']
        name = self.tree.item(self.tree.selection())['text']
        query = 'delete from product where id=?'
        self.run_query(query,(id,))
        self.message['text'] = 'Producto {} (Id:{}) Borrado'.format(name,id)
        self.get_products()

    def pre_edit_product(self):
        self.message['text']=''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text']='Seleccion un Producto'
            return
        id = self.tree.item(self.tree.selection())['open']
        name = self.tree.item(self.tree.selection())['text']
        price = self.tree.item(self.tree.selection())['values'][0]
        price = price.strip("$")
        old_price = price        

        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Editar Producto'       

        Label(self.edit_wind,text = 'Editar Producto').grid(row=0, column=1,sticky=E,padx=10,pady=10)       

        Label(self.edit_wind,text = 'ID de Producto: ').grid(row=1, column=1,sticky=E,padx=10,pady=10)
        id = Entry(self.edit_wind,textvariable = StringVar(self.edit_wind,value=id), state = 'readonly')
        id.grid(row='1',column='2')

        Label(self.edit_wind,text = 'Name: ').grid(row=2, column=1,padx=10,pady=10,sticky=E)
        Entry(self.edit_wind,textvariable = StringVar(self.edit_wind,value=name), state = 'readonly').grid(row='2',column='2',padx=10)
        Label(self.edit_wind,text = 'New Name: ').grid(row=3, column=1,padx=10,pady=10,sticky=E)
        new_name = Entry(self.edit_wind,textvariable = StringVar(self.edit_wind,value=name))
        new_name.grid(row='3',column='2',padx=10)

        Label(self.edit_wind,text = 'Price: $').grid(row=4, column=1,padx=10,pady=10,sticky=E)
        Entry(self.edit_wind,textvariable = StringVar(self.edit_wind,value=price), state = 'readonly').grid(row='4',column='2',padx=10)
        Label(self.edit_wind,text = 'New Price: $').grid(row=5, column=1,padx=10,pady=10,sticky=E)
        new_price = Entry(self.edit_wind,textvariable = StringVar(self.edit_wind,value=price))
        new_price.grid(row='5',column='2',padx=10)
        
        ttk.Button(self.edit_wind, text='Cerrar', command= self.close_edit_product).grid(row=6,column=1,sticky=W+E,padx=10, pady=10)

        ttk.Button(self.edit_wind, text='Actualizar Producto', command=lambda: self.edit_product(id.get(),new_name.get(),new_price.get())).grid(row=6,column=2,sticky=W+E,padx=10, pady=10)
        
    
    def close_edit_product(self):
        self.message['text'] = ''
        self.edit_wind.destroy()

    def edit_product(self,id,new_name,new_price):
        try:
            new_price = float(new_price)

            if id == '':
                self.edit_wind.destroy()
                self.message['text'] = 'Error Fatal'
            else:
                if new_name != '' and new_price != '':
                    query = 'Update product set name = ?, price = ? where id = ?'
                    #print(query)
                    parameters = (new_name, new_price, id)
                    self.run_query(query,parameters)
                    self.edit_wind.destroy()
                    self.message['text'] = 'Producto ({}) Actualizado'.format(new_name)
                    self.get_products()
                else:
                    self.message['text'] = 'Falta Nombre o Precio'
        except:
            self.message['text'] = 'Solo Numeros en Precio'
            

#end class ListaDeProductos: 

class AlinearVentana:

    def __init__(self, window):
        AlinearVentana.alinear_esquina_superior_izquierda(window)

    def alinear_esquina_superior_izquierda(self):
        self.geometry("+0+0")

    def alinear_esquina_inferior_derecha(self):
        self.geometry("-0-0")

    def alinear_esquina_inferior_izquierda(self):
        self.geometry("+0-0")

    def alinear_esquina_superior_derecha(self):
        self.geometry("-0+0")

    def centrar(self):
        altura = self.winfo_reqheight()
        anchura = self.winfo_reqwidth()
        altura_pantalla = self.winfo_screenheight()
        anchura_pantalla = self.winfo_screenwidth()
        print(f"Altura: {altura}\nAnchura: {anchura}\nAltura de pantalla: {altura_pantalla}\nAnchura de pantalla: {anchura_pantalla}")
        x = (anchura_pantalla // 2) - (anchura//2)
        y = (altura_pantalla//2) - (altura//2)
        self.geometry(f"+{x}+{y}")

#end class AlinearVentana: 


class ImprimeHora:      

    def __init__(self, window):        
        window.hora = Label(text = '', font=f"Arial 12", fg = 'blue')
        window.hora.grid(row=0,column=3,columnspan=2,sticky=E)
        ImprimeHora.actualiza_hora()

    def actualiza_hora():
        hora_actual = datetime.now().strftime("%H:%M:%S")
        window.after(1000, ImprimeHora.actualiza_hora)
        window.hora['text'] = hora_actual        

#end class ImprimeHora:


class ImprimeContador:

    def __init__(self,window):
        window.lcontador = Label(text = 'Contador', font=f"Arial 10", fg = 'brown')
        window.lcontador.grid(row=0,column=0,sticky=E)

        window.contador = Label(text = '0', font=f"Arial 10", fg = 'brown')
        window.contador.grid(row=0,column=1,sticky=W)    
        ImprimeContador.actualiza_contador()

    def actualiza_contador():
        contador = int(window.contador['text'])
        if contador>10:
            window.contador['text'] = 0
        else:
            window.contador['text'] =int(contador) + 1
        window.after(1000, ImprimeContador.actualiza_contador)
        
#end class ImprimeContador:




if __name__ == '__main__':

    window = Tk()    
    #window.attributes('-topmost', True)
    

    ConstruyeInterfaz(window)
    AlinearVentana(window)
    ImprimeHora(window)
    ImprimeContador(window)
    
    

    window.mainloop()
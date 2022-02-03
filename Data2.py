
__author__ = '7592047, Khauto'

class Data:

    in_stock = []

    def __init__(self, name='', type1='', categorie='', price=''):
        self.name = name
        self.type = type1
        self.categorie = categorie
        self.__price = price
        self.data = []
        self.counter = 1


    def calculate_cost(self):
        self.cost = 0
        for i in self.in_stock:
            self.cost = self.cost + (i.get_price()*i.counter)
        return self.cost

    def put_in_stock(self, object1):

        if not isinstance(object1, Data):
            raise TypeError('Object must be from class Data')
        if object1 not in self.in_stock:
            self.in_stock.append(object1)
        else:
            object1.counter += 1

    def remove_from_stock(self, object1):
        if not isinstance(object1, Data):
            raise TypeError('Object must be from class Data')
        if object1.counter > 1:
            object1.counter -= 1
        else:
            self.in_stock.remove(object1)

    def get_price(self):
        return float(self.__price)

    def read_file(self):
        with open('food.csv', 'r') as f1:
            reader = f1.readlines()
            list1 = []
            for line in reader:
                list1.append(line.split(';'))

            for i in list1:
                i[3] = i[3].replace('\n','')
                i[3] = i[3].replace(',', '.')
                i[3] = i[3].replace(' ', '')
            list1[0][1] = list1[0][1].replace(' ', '')
        return list1


    def create_objects(self):
        list1 = self.read_file()
        for i in range(1, len(list1)):
            object = Data(list1[i][0], list1[i][1], list1[i][2], list1[i][3])
            self.data.append(object)


    def create_bill(self):
        self.bill = []
        self.bill_str = '\n\n'

        for object in self.in_stock:
           self.bill.append(
            f'{object.counter}x {object.name}, \'{object.type}\', \'{object.categorie}\' = {object.get_price() * object.counter}€\n'
            )

        for i in self.bill:
            self.bill_str = self.bill_str + i +'\n'

        self.bill_str = self.bill_str + '****************************************************\n\n'
        self.bill_str = self.bill_str + f'Total cost = {self.calculate_cost()}€ \n\n'
        self.bill_str = self.bill_str + 'Thank you for buying!\n\n'

        return self.bill_str

    def clear_stock(self):
        self.obj_list = []
        for obj in self.in_stock:
            for i in range(obj.counter):
                self.obj_list.append(obj)

        for obj1 in self.obj_list:
            self.remove_from_stock(obj1)


    def get_data(self):
        return self.data

    def order(self):
        
        self.bill = self.create_bill()

        print('\nSuccessfuly ordered! \n' + self.bill)


def main():

    f = Data()
    f.create_objects()
    f.put_in_stock(f.data[0])
    f.put_in_stock(f.data[0])
    f.put_in_stock(f.data[0])
    f.put_in_stock(f.data[1])
    f.put_in_stock(f.data[1])
    f.put_in_stock(f.data[2])
    f.put_in_stock(f.data[11])
    f.remove_from_stock(f.data[0])
    f.remove_from_stock(f.data[0])
    #f.clear_stock()
    f.put_in_stock(f.data[1])
    f.put_in_stock(f.data[1])
    f.put_in_stock(f.data[11])
    print(f.in_stock)

    f.order()


if __name__ == '__main__':
    main()







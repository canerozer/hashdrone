from data_process import warehouse, order, drone

def parse(filename):
    FILENAME = filename
    GRIDSIZE = [0,0]
    N_DRONE = 0
    TURN = 0
    MAX_WEIGHT = 0
    N_PRODUCTS = 0
    PRODUCTS_WEIGHTS = list()

    warehouse_list = list()
    order_list = list()
    drone_list = list()

    with open(FILENAME, 'rb') as f:
        GRIDSIZE[0], GRIDSIZE[1], N_DRONE, TURN, MAX_WEIGHT = [int(i) for i in f.readline().split()]
        N_PRODUCTS = int(f.readline())
        PRODUCTS_WEIGHTS = [int(i)  for i in f.readline().split()]
        for x in xrange(int(f.readline())):
            position = [int(i) for i in f.readline().split()]
            warehouse_list.append(warehouse(position, [int(i) for i in f.readline().split()]))
        for x in xrange(int(f.readline())):
            position = [int(i) for i in f.readline().split()]
            dummy = f.readline()
            order_list.append(order(position, [int(i) for i in f.readline().split()], N_PRODUCTS))
    drone_list = [drone(warehouse_list[0].position, N_PRODUCTS) for i in xrange(N_DRONE)]

    return warehouse_list, order_list, drone_list

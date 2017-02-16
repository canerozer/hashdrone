import numpy as np
import parser as pr



def spatial_constraint(x, y, data):
    data = np.sqrt(np.array([(x-datum.position[0])**2+(y-datum.position[1])**2 for datum in data]).astype(np.float32))
    return np.argmin(data)

def weight_constraint(drone, i_prod, n_product, max_weight, prod_catalogue):
    pw = prod_catalogue[i_prod]
    available = max_weight-drone.weight
    return n_product if (available)/pw>=n_product else int(available/pw)
# rewardcuyu uyarmayi unutma

#supremum&infimum constraint

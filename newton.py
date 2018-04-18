import numpy as np


class planet():
        __init__(self, n_planet, n_mass, n_pos, n_v, delta_t):

                self.n_planet = n_planet
                self.n_mass = n_mass
                self.n_pos = n_pos
        self.n_v = n_v
        self.delta_t = delta_t

    def cal_force(self):
        f_x = 0
        f_y = 0
        f_z = 0
        
        for i in range(n_planet):
            for j in range(n_planet):

                if j == i:
                    continue
                else:
                    mass_prod = n_mass[i] * n_mass[j]
                    r_3 = np.sum((n_pos[i][-1] - n_pos[j][-1])**3)

                    f_x += mass_prod / r_3 * (n_pos[j][-1][0] - n_pos[i][-1][0])
                    f_y += mass_prod / r_3 * (n_pos[j][-1][1] - n_pos[i][-1][1])
                    f_z += mass_prod / r_3 * (n_pos[j][-1][2] - n_pos[i][-1][2]) 
            
            self.force[i] = np.array([f_x, f_y, f_z])


        return np.array([f_x, f_y, f_z])            

    def update_pos(self):
        #update the position of every planet
        for i in range(n):
            a = self.force[i] / self.n_mass[i]
            
            v_x_next = self.n_v[i][0] + a[0] * self.delta_t
            v_y_next = self.n_v[i][1] + a[1] * self.delta_t
            v_z_next = self.n_v[i][2] + a[2] * self.delta_t


            x = n_pos[i][-1][0] + (n_v[i][-1][0] + v_x_next)/2 * self.delta_t
            y = n_pos[i][-1][1] + (n_v[i][-1][1] + v_y_next)/2 * self.delta_t
            z = n_pos[i][-1][2] + (n_v[i][-1][2] + v_z_next)/2 * self.delta_t

            np.append(self.n_pos[i], np.array([[x, y, z]])
            np.append(self.n_v[i], np.array([[v_x_next, v_y_next, v_z_next]])

n = 2
n_mass = np.array([1,5])
n_pos = np.array([[1,1,1], [0, 0, 0]])
n_v = np.array([[0.5, 0.5, 0.5], [0.1, 0.1, 0.1]])
delta_t = 0.1


model = planet(n, n_mass, n_pos, n_v, delta_t)

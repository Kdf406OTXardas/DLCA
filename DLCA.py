import numpy as np
import random as rnd

def print_str(a,b):
    print(str(a),b)
    
rand_final=[]
random_list =[]
count_point=5
max=5
field_test = np.zeros((max+2,max+2))
list_for_check_calculate = np.array([-1, 0, 1])

def new_field():
    global max
    for x_rand in range(max):
        for y_rand in range(max):
            random_list.append([x_rand+1,y_rand+1])
    print_str(random_list,'random_list')


class Point(object):
        
    _registry={}
        
    def __init__(self ,num_globul ,coords):
        self._registry[num_globul] = {'coords' : coords}
        self.coords = coords
        self.num_globul = num_globul
        
    def add_coords(self,coords):
        self.coords.append(coords)
            
    @classmethod 
    def remove_point(self ,num_globul):
        self._registry.pop(num_globul)

def new_check_list():
    global check_list
    check_list = []
    for x in list_for_check_calculate:
        for y in list_for_check_calculate:
            for z in list_for_check_calculate:
                check_list.append([x,y])
    check_list.remove([0,0])     
    print_str(check_list, 'check_list')
    
def new_points():
    num_particle=0 
    for i in range(count_point):
        new_particle = rnd.choice(random_list)
        rand_final.append(new_particle)
        random_list.remove(new_particle)
        # print(new_particle)
        num_particle+=1
        globals()['point_' + str(num_particle)]=Point(num_particle ,[[new_particle[0],new_particle[1]]])
    print_str(Point._registry,'Point._registry')
    
def new_field_test():
    for k,v in Point._registry.items():
        print(v)#координата частицы
        print(k)#номер частицы
        print(v['coords'])
        for i in v['coords']:
            field_test[i[0]][i[1]]=k

    print(field_test,'field_test')    
    
    
    
def check_neighbourds():
    print_str(Point._registry,'до проверки')
    list_for_delete=[]
    #========= Проверка соседей (начало) =========
    for k,v in Point._registry.items():
        
        num_globul=k
        
        for x in list_for_check_calculate:
            for y in list_for_check_calculate:
                if ((abs(x)+abs(y)) !=0)==True:
                    for i in v['coords']:
                        if ((field_test[i[0]+x][i[1]+y] != num_globul) and (field_test[i[0]+x][i[1]+y]!=0))==True:
                                
                            for_delete = field_test[i[0]+x][i[1]+y] 
                            check_num_globul=field_test[i[0]][i[1]]
                            
                            print('test_1 finished')
                            
                            if (field_test[i[0]+x][i[1]+y]>check_num_globul)==True:
                                
                                list_for_delete.append(for_delete)   #добавление в список для удаления 
                                
                                for_relocation = Point._registry[for_delete]['coords']
                                        
                                print_str(for_delete,'for_delete')        
                                        
                                field_test[i[0]+x][i[1]+y]=check_num_globul
                                print('test_2 finished')
                                
                                for rel_point in for_relocation:
                                    exec('point_'+ str(check_num_globul)[:-2]+'.add_coords('+str(rel_point)+')')
                                    print_str(check_num_globul,'add_coords')
                                for_relocation = None
    print_str(Point._registry,'после проверки')

    for i in list_for_delete:
        Point.remove_point(i)

    print_str(Point._registry,'после удаления')     
    
    
def moving_point():
    print(field_test)
    if len(Point._registry)>0:
        for k,v in Point._registry.items():
            
            num_globul=k
            coord_moving = v['coords']
            # print(v['coords'])
                
            crit_mix_max=0
            stop_signal=0
            check_list_moving = check_list[:]
                
            if check_list_moving==[]:
                break
                    
            while (crit_mix_max==0 and stop_signal==0)==True:
                step_rnd = rnd.choices(check_list_moving)
                for_sum_coord=np.array(step_rnd)
                # print_str(step_rnd,' step_rnd')
                not_use=1
                # check_list_moving.remove(step_rnd[0])
                new_coord=coord_moving
            
                
                if step_rnd==[]:
                    new_coord=coord_moving
                    stop_signal=1
                    break
                refresh_value=[]
                for i in new_coord:
                    # print_str(i,' i')
                    t=i+for_sum_coord
                    # print_str(t,' t')
                    refresh_value.append(t.tolist()[0])
                    if ((t[0][0]<1 or t[0][1]<1
                        or t[0][0]>max or t[0][1]>max))==True:
                        not_use+=1
                        # print(check_list_moving)
                        # print(step_rnd)
                            
                if (not_use==1)==True:
                    
                    for i in v['coords']:
                        field_test[i[0]][i[1]]=0
                    
                    for i in refresh_value:
                        field_test[i[0]][i[1]]=num_globul
                    
                    # print(str(refresh_value), ' refresh_value')
                    crit_mix_max=1
                    
                    v['coords']= refresh_value
                    # print_str(v['coords'],'changed_point')
                    break
    else:
        print('расчет окончен')
    print("""
          ======================================================
          """)
    print(field_test)
    print_str(len(check_list),'- осталось свободных вариантов')



new_field()
# class_point()
new_check_list()
new_points()
new_field_test()
# print_str(check_list,'check_list')
# # while len(Point._registry)>1:
    # check_neighbourds()
    # moving_point()

check_neighbourds()
moving_point()
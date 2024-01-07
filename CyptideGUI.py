from tkinter import *
import math
from itertools import permutations 

class HexaCanvas(Canvas):
    """ A canvas that provides a create-hexagone method """
    def __init__(self, master, *args, **kwargs):
        Canvas.__init__(self, master, *args, **kwargs)
    
        self.hexaSize = 20
    
    def setHexaSize(self, number):
        self.hexaSize = number
    
    
    def create_hexagone(self, x, y, return_lines=False, size=None, color = "black", fill="blue", color1=None, color2=None, color3=None, color4=None, color5=None, color6=None, nolines=False):
        """ 
        Compute coordinates of 6 points relative to a center position.
        Point are numbered following this schema :
    
        Points in euclidiean grid:  
                    6
                    
                5       1
                    .
                4       2
            
                    3
    
        Each color is applied to the side that link the vertex with same number to its following.
        Ex : color 1 is applied on side (vertex1, vertex2)
    
        Take care that tkinter ordinate axes is inverted to the standard euclidian ones.
        Point on the screen will be horizontally mirrored.
        Displayed points:
    
                    3
              color3/      \color2      
                4       2
            color4|     |color1
                5       1
              color6\      /color6
                    6
        
        """
        if size is None:
            size = self.hexaSize
        Δx = (size**2 - (size/2)**2)**0.5
    
        # point1 = (x+Δx, y+size/2)
        # point2 = (x+Δx, y-size/2)
        # point3 = (x   , y-size  )
        # point4 = (x-Δx, y-size/2)
        # point5 = (x-Δx, y+size/2)
        # point6 = (x   , y+size  )

        point1 = (x+size/2, y+Δx)
        point2 = (x-size/2, y+Δx)
        point3 = (x-size  , y  )
        point4 = (x-size/2, y-Δx)
        point5 = (x+size/2, y-Δx)
        point6 = (x+size  , y  )

        # point1 = (y+size/2, x+Δx)
        # point2 = (y-size/2, x+Δx)
        # point3 = (y-size, x     )
        # point4 = (y-size/2, x-Δx)
        # point5 = (y+size/2, x-Δx)
        # point6 = (y+size, x     )
    
        #this setting allow to specify a different color for each side.
        if color1 == None:
            color1 = color
        if color2 == None:
            color2 = color
        if color3 == None:
            color3 = color
        if color4 == None:
            color4 = color
        if color5 == None:
            color5 = color
        if color6 == None:
            color6 = color

        if nolines is False:
            l1=self.create_line(point1, point2, fill=color1, width=5)
            l2=self.create_line(point2, point3, fill=color2, width=5)
            l3=self.create_line(point3, point4, fill=color3, width=5)
            l4=self.create_line(point4, point5, fill=color4, width=5)
            l5=self.create_line(point5, point6, fill=color5, width=5)
            l6=self.create_line(point6, point1, fill=color6, width=5)

        if return_lines:
            return [l1,l2,l3,l4,l5,l6]
        else:
            if fill != None:
                return self.create_polygon(point1, point2, point3, point4, point5, point6, fill=fill)
            else:
                return None
    
    def create_triangle(self, x, y, size=None, color = "black", fill="blue", color1=None, color2=None, color3=None, nolines=False):

        if size is None:
            size = self.hexaSize

        h=math.tan(30.*math.pi/180.)*size/2

        # point1 = (y, x-h)
        # point2 = ( y+size/4, x+h)
        # point3 = ( y-size/4, x+h)
        point1 = (x,y-2*h)
        point2 = (x+size/2, y+h)
        point3 = (x-size/2, y+h)
    
        #this setting allow to specify a different color for each side.
        if color1 == None:
            color1 = color
        if color2 == None:
            color2 = color
        if color3 == None:
            color3 = color
    
        if nolines is False:    
            l1=self.create_line(point1, point2, fill=color1, width=5)
            l2=self.create_line(point2, point3, fill=color2, width=5)
            l3=self.create_line(point3, point1, fill=color3, width=5)
    
        if fill != None:
            #print(self.create_polygon(point1, point2, point3, fill=fill))
            return [self.create_polygon(point1, point2, point3, fill=fill),l1,l2,l3]
    
    def create_cube(self, x, y, size=None, color = "black", fill="blue", color1=None, color2=None, color3=None, color4=None):

        if size is None:
            size = self.hexaSize

        s=size/2

        point1 = (x-s,y-s)
        point2 = (x-s, y+s)
        point3 = (x+s, y+s)
        point4 = (x+s, y-s)
    
        #this setting allow to specify a different color for each side.
        if color1 == None:
            color1 = color
        if color2 == None:
            color2 = color
        if color3 == None:
            color3 = color
        if color4 == None:
            color4 = color
      
        l1=self.create_line(point1, point2, fill=color1, width=5)
        l2=self.create_line(point2, point3, fill=color2, width=5)
        l3=self.create_line(point3, point4, fill=color3, width=5)
        l4=self.create_line(point4, point1, fill=color3, width=5)
    
        if fill != None:
            return [self.create_polygon(point1, point2, point3, point4, fill=fill),l1,l2,l3,l4]

    def create_octogone(self, x, y, size=None, fill="blue", color1=None, color2=None, color3=None, color4=None, color5=None, color6=None, nolines=False):
        """I cheese it into a circle"""
        def create_circle(x, y, r, **kwargs): #center coordinates, radius
            x0 = x - r
            y0 = y - r
            x1 = x + r
            y1 = y + r
            return self.create_oval(x0, y0, x1, y1, width=5,**kwargs)
        c=create_circle(x, y, 15, fill=fill)
        return [c]


class HexagonalGrid(HexaCanvas):
    """ A grid whose each cell is hexagonal """
    def __init__(self, master, scale, grid_width, grid_height, *args, **kwargs):
    
        Δx     = (scale**2 - (scale/2.0)**2)**0.5
        width  = 2 * Δx * grid_width + Δx
        height = 1.5 * scale * grid_height + 0.5 * scale
        #width=1.5 * scale * grid_height + 0.5 * scale
        #height=2 * Δx * grid_width + Δx

        HexaCanvas.__init__(self, master, background='white', width=width, height=height, *args, **kwargs)
        self.setHexaSize(scale)

        self.elements = []
        self.elts2del = []
        self.cubes =[]
    
    def setCell(self, xCell, yCell, idx=None, terrain=None, type=None, fill=None, *args, **kwargs ):
        """ Create a content in the cell of coordinates x and y. Could specify options throught keywords : color, fill, color1, color2, color3, color4; color5, color6"""
    
        #compute pixel coordinate of the center of the cell:
        size = self.hexaSize
        Δx = (size**2 - (size/2)**2)**0.5
    
        # pix_x = Δx + 2*Δx*xCell
        # if yCell%2 ==1 :
        #     pix_x += Δx
        pix_y=Δx + 2*Δx*xCell
        if yCell%2 ==1 :
            pix_y += Δx
    
        # Add 5 to avoid clipping on top row of hexes
        #pix_y = size + yCell*1.5*size + 5
        pix_x = size + yCell*1.5*size + 5

        if type=='hex':
            if idx is not None:
                self.elements[idx-1]['building']={'shape':type,'color':fill}
            return self.create_octogone(pix_x, pix_y, fill=fill,*args, **kwargs)
        if type=='tri':
            if idx is not None:
                self.elements[idx-1]['building']={'shape':type,'color':fill}
            return self.create_triangle(pix_x, pix_y, fill=fill,*args, **kwargs)

        if type=='animal_ter':
            self.create_hexagone(pix_x, pix_y, fill=fill,*args, **kwargs)
            self.elements[idx-1]['ter']=terrain
        if type=='sol':
            self.elts2del.append(self.create_hexagone(pix_x, pix_y, fill=fill,*args, **kwargs))
        if type=='ens':
            self.elts2del.append(self.create_hexagone(pix_x, pix_y, return_lines=True, fill=fill,*args, **kwargs))
        if type is None:
            self.create_hexagone(pix_x, pix_y, fill=fill,*args, **kwargs)
            self.elements.append({'id':idx,'type':terrain,'ter':None,'building':None,'center':[pix_x,pix_y]})
        
        if type=='cube':
            if idx is not None:
                self.elements[idx-1]['cube']={'shape':type,'color':fill}
            return self.create_cube(pix_x, pix_y, fill=fill,*args, **kwargs)
        
        if type=='circle':
            if idx is not None:
                self.elements[idx-1]['circle']={'shape':type,'color':fill}
            return self.create_octogone(pix_x, pix_y, fill=fill,*args, **kwargs)


class Utils():

    def who_is_reversed(self):
        i=1
        L=[]
        q=int(input("how many reversed?"))
        #q=4
        for k in range (0,q):
            i=int(input("who is reversed?"))
            L.append(i)
        #L=[4,3,1,6]
        return L
    def reverseconfig(self, types, ters):
        L=self.who_is_reversed()
        for key in types:
            if int(key) in L:
                types[key].reverse()
                tmp_dic=ters[key].copy()
                for cle in tmp_dic:
                    new_cle = 19-int(cle)
                    ters[key][new_cle]=ters[key][cle]
                    del ters[key][cle]
    
    def global_positionning(self):
        d={}
        D={}
        for i in range (0,6):
            k=int(input("who is in position "+str(i)+" ?"))
            d[i]=k
            D[k]=i
        #d={0:4, 1:3, 2:5, 3:2, 4:1, 5:6}
        #D={1:4, 2:3, 3:1, 4:0, 5:2, 6:5}
        return d, D
    
    def loc2glob(self,i,j,gi,gj,sx,sy):
        return (i+gi*sx,j+gj*sy)
    
    # def building_positionning(self,objs):
    #     u_objects={}
    #     for obj in objs:
    #         coord=input(str(obj)+" coordonates? (ex: 2,1 or 2,10 and None if none)")
    #         if coord != "None":
    #             coord=tuple(map(int, coord.split(',')))
    #             g_idx=coord[1]+g2[coord[0]]*18
    #             u_objects[g_idx]=obj
    #     return u_objects

class Connectivity():
    def __init__(self):
        self.loc_connect={1:[7,2], 2:[1,3,7,8,9], 3:[2,9,4], 4:[3,9,10,11,5], 5:[4,11,6], 6:[5,11,12], 7:[1,2,8,13], 8:[7,2,9,15,14,13], 
                          9:[2,3,4,10,15,8], 10:[9,4,11,17,16,15], 11:[4,5,6,12,17,10], 12:[6,11,17,18], 13:[7,8,14], 14:[13,8,15], 
                          15:[14,8,9,10,16], 16:[15,10,17], 17:[16,10,11,12,18], 18:[17,12]}
        self.glob_ops={0:[(1,'lr'), (2, 'ud'), (3, 'tr')], 1:[(3,'ud')], 2:[(3, 'lr'), (4, 'ud'), (5, 'tr')], 3:[(5,'ud')], 4:[(5, 'lr')]}
        self.glob_connect=self.global_connectivity(self.glob_ops, self.loc_connect)
        self.glob_connect = dict(sorted(self.glob_connect.items()))

        self.glob_connect_2=self.global_connectivity2()
        self.glob_connect_3=self.global_connectivity3()
    
    def global_connectivity2(self):
        glob_connect_2={}
        for key, value in self.glob_connect.items():
            glob_connect_2[key]=[]
            for val in value:
                if val not in glob_connect_2[key]:
                    glob_connect_2[key].append(val)
                for n in self.glob_connect[val]:
                    if n not in glob_connect_2[key] and n!=key:
                        glob_connect_2[key].append(n)
            
            glob_connect_2[key].sort()
        
        return glob_connect_2

    def global_connectivity3(self):
        glob_connect_2={}
        for key, value in self.glob_connect.items():
            glob_connect_2[key]=[]
            for val in value:
                if val not in glob_connect_2[key]:
                    glob_connect_2[key].append(val)
                for n in self.glob_connect[val]:
                    if n not in glob_connect_2[key] and n!=key:
                        glob_connect_2[key].append(n)
                    for m in self.glob_connect[n]:
                        if m not in glob_connect_2[key] and m!=key:
                            glob_connect_2[key].append(m)
            
            glob_connect_2[key].sort()
        
        return glob_connect_2

    def global_connectivity(self,glob_ops, loc_connect):
    
        glob_connect=loc_connect.copy()
        s=18

        #ajout des connectivités loc en glob
        for key, value in loc_connect.items():
            for k in range (1,6):
                glob_connect[key+k*s]=[]
                for i in value:
                    glob_connect[key+k*s].append(i+k*s)
        
        for key, value in glob_ops.items():
            for tupl in value:
                #print(tupl[1])
                connect=self.boundary_connectivity(tupl[1])
                #print(connect)
                for idx, elts in connect.items():
                    for jdx in elts:
                        self.link(idx+key*s, jdx+tupl[0]*s, glob_connect)
        
        return glob_connect

    def boundary_connectivity(self, string):
        if string=='lr':
            loc_lr_bound={6:[1,7],12:[7,13],18:[13]}
            return loc_lr_bound
        if string=='ud':
            loc_ud_bound={13:[1],14:[1,2,3],15:[3],16:[3,4,5],17:[5],18:[5,6]}
            return loc_ud_bound
        if string=='tr':
            loc_tr_bound={18:[1]}
            return loc_tr_bound
        else:
            return "AAAAAAAAAAhsasaaaaAAAAAAH"
    
    def link(self,i,k,diconect):
        if i in diconect:
            diconect[i].append(k)
        else:
            diconect[i]=[]
            diconect[i].append(k)

        if k in diconect:
            diconect[k].append(i)
        else:
            diconect[k]=[]
            diconect[k].append(i)

class Ensembles():
    def __init__(self, gmap, connectivity):
        #Is in field
        type_list_0=['forest', 'desert', 'swamp', 'mountain', 'lac']
        dico={}
        tuple_list=[]
        inc=0
        for type1 in type_list_0:
            for type2 in type_list_0:
                if type1!=type2:
                    tuple_list.append((type1,type2))
                    if (type2,type1) not in tuple_list:
                        tuple_list.append((type2,type1))
                        inc+=1
                        dico[inc]=[{'type':type1, 'order':0}, {'type':type2, 'order':0}]
        #In or first neighbour
        type_list_1=[[{'type':'forest', 'order':1}], [{'type':'desert', 'order':1}], [{'type':'swamp', 'order':1}], [{'type':'mountain', 'order':1}], [{'type':'lac', 'order':1}], 
        [{'ter':'bear', 'order':1}, {'ter':'puma', 'order':1}]]
        for type in type_list_1:
            inc+=1
            dico[inc]=type
        #In or second neighbour
        ['hex', 'tri', 'bear', 'puma']
        type_list_2=[[{'building':{'shape':'hex'}, 'order':2}], [{'building':{'shape':'tri'}, 'order':2}], [{'ter': 'bear', 'order':2}], 
                    [{'ter': 'puma', 'order':2}]]

        for type in type_list_2:
            inc+=1
            dico[inc]=type
        #In or third neighbour
        type_list_3=[[{'building':{'color':'white'}, 'order':3}], [{'building':{'color':'blue'}, 'order':3}], [{'building':{'color':'green'}, 'order':3}]]

        for type in type_list_3:
            inc+=1
            dico[inc]=type

        self.dico=dico
        self.ensembles=self.create_ensembles(gmap, connectivity)


    def create_ensembles(self, gmap, connectivity):

        ensembles_dic={}
        for key, value in self.dico.items():
            order=value[0]['order']
            L=self.subfunc(value, order, gmap, connectivity)
            ensembles_dic[key]=L   
            
        return ensembles_dic
    
    def subfunc(self, val, order, gmap, connectivity):
        glob_connect=connectivity.glob_connect
        glob_connect_2=connectivity.glob_connect_2
        glob_connect_3=connectivity.glob_connect_3

        L=[]
        if order==0:
            for elt in val:
                for case in gmap:
                    if elt['type']==case['type']:
                        L.append(case['id'])
            L.sort()
            return L
        if order==1:
            for elt in val:
                if 'type' in elt:
                    for case in gmap:
                        if elt['type']==case['type']:
                            if case['id'] not in L:
                                L.append(case['id'])
                            for id in glob_connect[case['id']]:
                                if id not in L:
                                    L.append(id)
                if 'ter' in elt:
                    for case in gmap:
                        if elt['ter']==case['ter']:
                            if case['id'] not in L:
                                L.append(case['id'])
                            for id in glob_connect[case['id']]:
                                if id not in L:
                                    L.append(id)
                            
            L.sort()
            return L
        if order==2:
            for elt in val:
                if 'building' in elt:
                    for case in gmap:
                        if case['building'] is not None:
                            if elt['building']['shape']==case['building']['shape']:
                                if case['id'] not in L:
                                    L.append(case['id'])
                                for id in glob_connect_2[case['id']]:
                                    if id not in L:
                                        L.append(id)
                if 'ter' in elt:
                    for case in gmap:
                        if elt['ter']==case['ter']:
                            if case['id'] not in L:
                                L.append(case['id'])
                            for id in glob_connect_2[case['id']]:
                                if id not in L:
                                    L.append(id)
            L.sort()
            return L
        else:
            for elt in val:
                if 'building' in elt:
                        for case in gmap:
                            if case['building'] is not None:
                                if elt['building']['color']==case['building']['color']:
                                    if case['id'] not in L:
                                        L.append(case['id'])
                                    for id in glob_connect_3[case['id']]:
                                        if id not in L:
                                            L.append(id)
            return L

class Solve():
    def __init__(self, ens, p=3, clue=1):
        self.p=p
        self.clue=clue
        self.ens=ens
        self.res={}
    
    def solve(self):
        if self.p==3:
            for key, value in self.ens.items():
                if self.ens[self.clue]!=value:
                    intersect=self.intersection(self.ens[self.clue], value)
                    for k, v in self.ens.items():
                        if v!=value:
                            intersect2=self.intersection(intersect, v)
                            #print(intersect2)
                            if len(intersect2)==1:
                                if intersect2[0] not in self.res:
                                    #res[intersect2[0]]={'known_clue':clue, 'unknown_clue_1':key, 'unknown_clue_2':k}
                                    self.res[intersect2[0]]=[]
                                    t=[key, k]
                                    t.sort()
                                    if t not in self.res[intersect2[0]]:
                                        self.res[intersect2[0]].append(t)
                                else:
                                    t=[key, k]
                                    t.sort()
                                    if t not in self.res[intersect2[0]]:
                                        self.res[intersect2[0]].append(t)
                                    
        if self.p==4:
            for key, value in self.ens.items():
                if self.ens[self.clue]!=value:
                    intersect=self.intersection(self.ens[self.clue], value)
                    for k, v in self.ens.items():
                        if v!=value:
                            intersect2=self.intersection(intersect, v)
                            for b,n in self.ens.items():
                                if n!=v:
                                    intersect3=self.intersection(intersect2, n)
                                    if len(intersect3)==1:
                                        if intersect3[0] not in self.res:
                                            self.res[intersect3[0]]=[]
                                            t=[key, k, b]
                                            t = list(set(t))
                                            if len(t)!=3:
                                                continue
                                            t.sort()
                                            if t not in self.res[intersect3[0]]:
                                                self.res[intersect3[0]].append(t)
                                        else:
                                            #res[intersect3[0]].append({'known_clue':clue, 'unknown_clue_1':key, 'unknown_clue_2':k, 'unknown_clue_3':b})
                                            t=[key, k, b]
                                            t = list(set(t))
                                            if len(t)!=3:
                                                continue
                                            t.sort()
                                            if t not in self.res[intersect3[0]]:
                                                self.res[intersect3[0]].append(t)
        if self.p==5:
            print('not yet implemented')

    def intersection(self, l1, l2):
        l=[]
        for a in l1:
            for b in l2:
                if a==b:
                    l.append(a)
        l.sort()
        return l


class Research(Solve):
    def __init__(self, ens, res, imp_clues):
        self.count=self.counter(res)
        research_dic={}
        for key, value in self.count.items():
            research_dic[key]=ens[key]
        self.research_dic=research_dic

        #self.adv_res, self.buffer_res=self.advanced_research(c_num=c_num)

        poss_clues=self.possible_clues(imp_clues,ens)
        dic_of_colors={}
        for k, clue_list in poss_clues.items():
            research_dic_color={}
            for clue in clue_list:
                if clue in self.count:
                    research_dic_color[clue]=ens[clue]
            dic_of_colors[k]=research_dic_color
        self.dic_of_colors=dic_of_colors

    def advanced_research(self, research_dic, c_num):
        adv_res={}
        perm=permutations(research_dic, c_num)
        
        long=self.maxlength(research_dic)
        pbuffer=0
        Lbuffer=[]
        for p in list(perm):
            small_dic={}
            for s in list(p):
                small_dic[s]=research_dic[s]
            l=small_dic[list(small_dic.keys())[0]]
            L=self.collapse(l,small_dic)
            if len(L)<long and len(L)>0:
                pbuffer=p
                Lbuffer=L
                long=len(L)
                #if len(L)==1:
                    #adv_res[p]={'list':L, 'long':long}
            adv_res[p]={'list':L, 'long':long}
        buffer_res={'clues':pbuffer,'list':Lbuffer, 'long':long}
    
        return adv_res, buffer_res
    #nice print of dico2ask
    def nice_print(self,dico):
        for key, el in dico.items():
            print(key)
            for e in el:
                print(e)
            print('#')
            print('#')
    def dico2ask(self,cube_percol):
        # dico2ask={}
        # for color in list(cube_percol.keys()):
        #     research_dic_color=self.dic_of_colors[color]
        #     c_num=1
            
        #     dico_adv, buffer = self.advanced_research(research_dic_color, c_num)
        #     while len(buffer['list'])>1 and c_num+1<len(research_dic_color):
        #         #print(c_num)
        #         c_num+=1
        #         dico_adv, buffer= self.advanced_research(research_dic_color, c_num)
        #     dico2ask[color]=buffer
        # print(dico2ask)
        dico2ask={}
        for color in list(cube_percol.keys()):
            research_dic_color=self.dic_of_colors[color]

            while len(research_dic_color)>1:
                c_num=1
                dico_adv, buffer = self.advanced_research(research_dic_color, c_num)
                while len(buffer['list'])>1 and c_num<len(research_dic_color) and c_num<5:
                    #print(c_num)
                    dico_adv, buffer= self.advanced_research(research_dic_color, c_num)
                    c_num+=1
                if color not in dico2ask:
                    dico2ask[color]=[buffer]
                else:
                    dico2ask[color].append(buffer)
                clues2del=buffer['clues']
                if clues2del!=0:
                    #print(clues2del)
                    for clue in clues2del:
                        del research_dic_color[clue]
                #print(len(research_dic_color))
            if len(research_dic_color)==1:
                if color not in dico2ask:
                    dico2ask[color]=[{'clues':list(research_dic_color.keys())[0], 'list':research_dic_color[list(research_dic_color.keys())[0]]}]
                else:
                    dico2ask[color].append({'clues':list(research_dic_color.keys())[0], 'list':research_dic_color[list(research_dic_color.keys())[0]]})
        self.nice_print(dico2ask)

    def possible_clues(self, imp_clues, ens):
        dico={}
        for color, clue_list in imp_clues.items():
            for clue in list(ens.keys()):
                if clue not in clue_list:
                    if color in dico:
                        dico[color].append(clue)
                        dico[color].sort()
                    else:
                        dico[color]=[clue]
                    
        return dico

    def maxlength(self, dico):
        if dico:
            l=len(dico[list(dico.keys())[0]])
            for k,v in dico.items():
                if len(v)>l:
                    l=len(v)
        else:
            l=0
        return l
    
    def collapse(self, l,research_dic,i=0):
        keys=list(research_dic.keys())
        if i+1==len(keys):
            return l
        l=self.intersection(l, research_dic[list(research_dic.keys())[i+1]])
        i+=1
        if len(l)<=1:
            return l
        return self.collapse(l,research_dic,i)
    def counter(self, res):
        dico_compter={}
        for key, value in res.items():
            for t in value:
                for clue in t:
                    if clue in dico_compter:
                        dico_compter[clue]+=1
                    else:
                        dico_compter[clue]=1
        l=sorted(dico_compter.items(), key=lambda x:x[1], reverse=True)
        return_dic={}
        for elt in l:
            return_dic[elt[0]]=elt[1]
            
        return return_dic

class Building():
    def __init__(self,objs):
        self.objs=objs
        self.buildings={}
        self.counter=0

        self.currdisplay=[]
        self.display()

    def display(self):
        self.currdisplay=grid.setCell(5,13, type=self.objs[self.counter]['shape'],size=40, fill=self.objs[self.counter]['color'])
    
    def destroydisplay(self):
        for elt in self.currdisplay:
            grid.delete(elt)

class Cubes():
    def __init__(self,cubes):
        self.cubes=cubes
        self.cube_dico={}
        self.counter=0

class Evenements():
    def __init__(self, tk):
        self.tk=tk
    def correct_quit(self,tk):
        tk.destroy()
        tk.quit()
    def add_building(self,event,build):

        build.destroydisplay()

        #--------
        x, y = event.x, event.y
        dist_init=(x-elements[0]['center'][0])**2 + (y-elements[0]['center'][1])**2
        el_init=elements[0]['id']
        for el in elements:
            center=el['center']
            dist=(x-center[0])**2 + (y-center[1])**2
            if dist<dist_init:
                dist_init=dist
                el_init=el['id']
        #--------
        if build.counter<len(build.objs):
            build.buildings[el_init]=build.objs[build.counter]
            #euclidian division
            q=el_init//18 #global positionning
            r=el_init%18 #local positionning
            if r==0:
                r=18
                q-=1
            coord=glob2coord[q]
            idx_loc=loc2coord[r]
            idx_glob=u.loc2glob(idx_loc[0],idx_loc[1],coord[0],coord[1],3,6)
            grid.setCell(idx_glob[0],idx_glob[1],idx=el_init, type=build.objs[build.counter]['shape'],size=40, fill=build.objs[build.counter]['color'])
        else:
            print('No more buildings to put!')
        build.counter+=1
        if build.counter<len(build.objs):
            build.display()
    
    def add_cubes(self,event,build):
        #--------
        x, y = event.x, event.y
        dist_init=(x-elements[0]['center'][0])**2 + (y-elements[0]['center'][1])**2
        el_init=elements[0]['id']
        for el in elements:
            center=el['center']
            dist=(x-center[0])**2 + (y-center[1])**2
            if dist<dist_init:
                dist_init=dist
                el_init=el['id']
        #--------
        if build.counter<len(build.cubes):
            build.cube_dico[el_init]=build.cubes[build.counter]
            #euclidian division
            q=el_init//18 #global positionning
            r=el_init%18 #local positionning
            if r==0:
                r=18
                q-=1
            coord=glob2coord[q]
            idx_loc=loc2coord[r]
            idx_glob=u.loc2glob(idx_loc[0],idx_loc[1],coord[0],coord[1],3,6)
            grid.setCell(idx_glob[0],idx_glob[1],idx=el_init, type=build.cubes[build.counter]['shape'],size=15, fill=build.cubes[build.counter]['color'])
            
        else:
            build.counter=0
            build.cube_dico[el_init]=build.cubes[build.counter]
            #euclidian division
            q=el_init//18 #global positionning
            r=el_init%18 #local positionning
            if r==0:
                r=18
                q-=1
            coord=glob2coord[q]
            idx_loc=loc2coord[r]
            idx_glob=u.loc2glob(idx_loc[0],idx_loc[1],coord[0],coord[1],3,6)
            grid.setCell(idx_glob[0],idx_glob[1],idx=el_init, type=build.cubes[build.counter]['shape'],size=15, fill=build.cubes[build.counter]['color'])
        build.counter+=1
        #print(build.cube_dico)
        #print(grid.elements)

    def motion(self,event):
        x, y = event.x, event.y
        dist_init=(x-elements[0]['center'][0])**2 + (y-elements[0]['center'][1])**2
        el_init=elements[0]['id']
        for el in elements:
            center=el['center']
            dist=(x-center[0])**2 + (y-center[1])**2
            if dist<dist_init:
                dist_init=dist
                el_init=el['id']

        label=Label(tk,text=str(el_init),bg="white",borderwidth=1)
        label.grid(row=2, column=1, padx=5, pady=5)

class DisplaySolve(Solve):
    def __init__(self):
        self.label=Label(tk,text='',bg="white",borderwidth=1)
        self.has_solved=False
    def solve(self,event,elements,cubes,circles,c,*args,**kwargs):
        ens=Ensembles(elements,c)
        coord=reponse.get()
        coord=tuple(map(int, coord.split(',')))
        #print(coord)
        for elt in grid.elts2del:
                if(isinstance(elt,list)):
                    for id in elt:
                        grid.delete(id)
                else:
                    grid.delete(elt)
        #display clue
        if coord[0]==0:
            
            for k in ens.ensembles[coord[1]]:
                q=k//18 #global positionning
                r=k%18 #local positionning
                if r==0:
                    r=18
                    q-=1
                coord=glob2coord[q]
                idx_loc=loc2coord[r]
                idx_glob=u.loc2glob(idx_loc[0],idx_loc[1],coord[0],coord[1],3,6)
                grid.setCell(idx_glob[0],idx_glob[1],size=48,type='ens', fill=None, color1='white',color2='white',color3='white',color4='white',color5='white',color6='white')
        #solve and display
        else: 
            p=coord[0]
            your_color=coord[2]
            s=Solve(ens.ensembles, p=p, clue=coord[1], **kwargs)
            s.solve()
            if len(cubes.cube_dico)>=2*p:
                corr_res=self.correct_sol(s.res, ens.ensembles, cubes.cube_dico, cubes.cubes[your_color]['color'], circles.cube_dico)
            else:
                corr_res=s.res

            for cube in list(cubes.cube_dico.keys()):
                if cube in corr_res:
                    del corr_res[cube]

            print('result: '+str(corr_res))
            print('#')
            print('#')

            for k,v in corr_res.items():
                q=k//18 #global positionning
                r=k%18 #local positionning
                if r==0:
                    r=18
                    q-=1
                coord=glob2coord[q]
                idx_loc=loc2coord[r]
                idx_glob=u.loc2glob(idx_loc[0],idx_loc[1],coord[0],coord[1],3,6)
                grid.setCell(idx_glob[0],idx_glob[1],size=20,type='sol', fill='red', nolines=True)
            
            imp_clues=self.impossible_clues(self.get_cubepos_bycolor(cubes.cube_dico), self.get_cubepos_bycolor(circles.cube_dico), ens.ensembles)
            r=Research(ens.ensembles, s.res, imp_clues)
            r.dico2ask(self.get_cubepos_bycolor(cubes.cube_dico))
            #print(r.buffer_res)
    def get_cubepos_bycolor(self, cubes):
        dico={}
        for k,v in cubes.items():
            if v['color'] in dico:
                dico[v['color']].append(k)
            else:
                dico[v['color']]=[k]
        return dico
    ###impossible clues per color
    def impossible_clues(self, cube_percol, circle_percol, ens):
        dico={}
        #loop on cubes
        for color, elt_list in cube_percol.items():
            for elt in elt_list:
                for clue,ensemble in ens.items():
                    if elt in ensemble:
                        if color in dico:
                            if clue not in dico[color]:
                                dico[color].append(clue)
                                dico[color].sort()
                        else:
                            dico[color]=[clue]
        #loop on circles
        for color, elt_list in circle_percol.items():
            for elt in elt_list:
                for clue,ensemble in ens.items():
                    if elt not in ensemble:
                        if color in dico:
                            if clue not in dico[color]:
                                dico[color].append(clue)
                                dico[color].sort()
                        else:
                            dico[color]=[clue]
        return dico
    ###possible clues per color
    def possible_clues(self, imp_clues, ens):
        dico={}
        for color, clue_list in imp_clues.items():
            for clue in list(ens.keys()):
                if clue not in clue_list:
                    if color in dico:
                        dico[color].append(clue)
                        dico[color].sort()
                    else:
                        dico[color]=[clue]
                    
        return dico
    #do not use your own clue!!
    def check_if_false(self, clue, your_color, imp_clues):
        count=0
        for color, clue_list in imp_clues.items():
            if color==your_color:
                continue
            if clue in clue_list:
                count+=1
        
        c=len(imp_clues)-count
        if c==1:
            return True
        else:
            return False
    
    #returns only exclusive elts of l1 compared to l2
    def exclusion(self,l1,l2):
        l=[]
        for a in l1:
            if a not in l2:
                l.append(a)
        return l
    def exclusive_clues_percol(self, poss_clues, your_color):
        dico={}
        for color, clues in poss_clues.items():
            l=clues
            #print(l)
            if your_color==color:
                continue
            for col, clu in poss_clues.items():
                if your_color==color or col==color:
                    continue
                l=self.exclusion(l, clu)
                #print(l)
            dico[color]=l
        return dico
    #loop on poss_clues, return true if more than 1 clue of tupl is in same color
    def check_redundancy(self, tupl, poss_clues, your_color):
        for color, posclue in poss_clues.items():
            count=0
            #display only exclusive clues
            posclue=self.exclusive_clues_percol(poss_clues, self.your_color)
            for clue in posclue:
                if clue in tupl:
                    count+=1
            if count>=2:
                return True
        
        return False

    def correct_sol(self, res, ens, cubes, your_color, circles):        
        cube_percol=self.get_cubepos_bycolor(cubes)
        circle_percol=self.get_cubepos_bycolor(circles)
        imp_clues=self.impossible_clues(cube_percol, circle_percol, ens)
        poss_clues=self.possible_clues(imp_clues, ens)
        #remove by check if clue is false
        res_loop=res.copy()
        for sol, tupl_list in res_loop.items():
            tupl_list_loop=tupl_list.copy()
            for tupl in tupl_list_loop:
                for clue in tupl:
                    if self.check_if_false(clue, your_color, imp_clues):
                        if tupl in res[sol]:
                            res[sol].remove(tupl)
            if res[sol]==[]:
                del res[sol]
        
        #remove if redundancy of clue in one color's possible clue list
        res_loop=res.copy()
        for sol, tupl_list in res_loop.items():
            tupl_list_loop=tupl_list.copy()
            for tupl in tupl_list_loop:
                if self.check_redundancy(tupl,poss_clues,your_color):
                    if tupl in res[sol]:
                            res[sol].remove(tupl)
            if res[sol]==[]:
                del res[sol]

        return res


if __name__ == "__main__":
    tk = Tk()
    grid = HexagonalGrid(tk, scale = 50, grid_width=2*6, grid_height=3*3.8)
    grid.grid(row=1, column=0, padx=5, pady=5)
    u=Utils()

    #evenements
    e=Evenements(tk)

    quit = Button(tk, text = "Quit", command = lambda :e.correct_quit(tk))
    quit.grid(row=2, column=0)

    #Create Types
    types1=["lac","lac","lac","lac","forest", "forest", "swamp", "swamp", "lac", "desert", "forest", "forest", "swamp", "swamp", "desert", "desert", "desert", "forest"]
    types2=["swamp", "forest", "forest", "forest", "forest", "forest", "swamp", "swamp", "forest", "desert", "desert", "desert", "swamp", "mountain", "mountain", "mountain", "mountain", "desert"]
    types3=["swamp","swamp","forest","forest","forest","lac","swamp","swamp","forest","mountain","lac","lac","mountain","mountain","mountain","mountain","lac","lac"]
    types4=["desert", "desert","mountain","mountain","mountain","mountain","desert", "desert","mountain","lac","lac","lac","desert", "desert","desert","forest","forest","forest"]
    types5=["swamp","swamp","swamp","mountain","mountain","mountain","swamp","desert", "desert","lac","mountain","mountain","desert", "desert","lac","lac","lac","lac"]
    types6=["desert", "desert","swamp","swamp","swamp","forest","mountain","mountain","swamp","swamp","forest","forest","mountain","lac","lac","lac","lac","forest"]
    types = {1:types1, 2:types2, 3:types3, 4:types4, 5:types5, 6:types6}
    type2color={"lac":'blue', "forest":'green', "swamp":'brown', "mountain":'gray', "desert":'yellow'}

    #Create animal territory
    ter1={18:"bear", 17:"bear", 16:"bear"}
    ter2={1:"puma", 2:"puma", 3:"puma"}
    ter3={7:"puma", 8:"puma", 13:"puma"}
    ter4={12:"puma", 18:"puma"}
    ter5={12:"bear", 17:"bear", 18:"bear"}
    ter6={1:"bear", 7:"bear"}
    ters = {1:ter1, 2:ter2, 3:ter3, 4:ter4, 5:ter5, 6:ter6}
    ter2color={"bear":'black',"puma":'red'}

    #reverse
    u.reverseconfig(types,ters)

    #global positionning
    coord2loc={}
    inc=1
    for i in range (0,3):
        for k in range (0,6):
            coord2loc[(i,k)]=inc
            inc+=1

    g1,g2=u.global_positionning()
    glob2coord={0:(0,0), 1:(0,1), 2:(1,0), 3:(1,1), 4:(2,0), 5:(2,1)}
    for pos,id in g1.items():
        inc=0
        for i in range(0,3):
            for j in range(0,6):
                idx_glob=u.loc2glob(i,j,glob2coord[pos][0],glob2coord[pos][1],3,6)
                #print(type2color[types[id][inc]])
                grid.setCell(idx_glob[0],idx_glob[1],idx=coord2loc[(i,j)]+18*pos,terrain=types[id][inc],fill=type2color[types[id][inc]])
                inc+=1

    #animal positionning
    loc2coord={}
    inc=1
    for i in range (0,3):
        for k in range (0,6):
            loc2coord[inc]=(i,k)
            inc+=1

    for k,v in ters.items():
        pos=g2[k]
        coord=glob2coord[pos]
        for id, animal in v.items():
            idx_loc=loc2coord[id]
            idx_glob=u.loc2glob(idx_loc[0],idx_loc[1],coord[0],coord[1],3,6)
            grid.setCell(idx_glob[0],idx_glob[1],size=35, idx=id+18*pos,type='animal_ter',terrain=animal,fill=None, color1=ter2color[animal], color2=ter2color[animal], color3=ter2color[animal], color4=ter2color[animal], 
                         color5=ter2color[animal], color6=ter2color[animal])
    
    #building user input
    bluetri={"shape":"tri", "color":"blue"}
    bluehex={"shape":"hex", "color":"blue"}
    whitetri={"shape":"tri", "color":"white"}
    whitehex={"shape":"hex", "color":"white"}
    greentri={"shape":"tri", "color":"green"}
    greenhex={"shape":"hex", "color":"green"}
    blacktri={"shape":"tri", "color":"black"}
    blackhex={"shape":"hex", "color":"black"}
    objs_easy=[bluetri,bluehex,whitetri,whitehex,greentri,greenhex]
    objs_hard=[bluetri,bluehex,whitetri,whitehex,greentri,greenhex,blacktri,blackhex]

    #build=Building(objs_hard)
    build=Building(objs_easy)
    tk.bind('<Button-1>',lambda event:e.add_building(event,build))

    #motion of mouse
    tk.bind('<Motion>', e.motion)

    #get dico of all hexas
    elements=grid.elements

    #create connectivity
    c=Connectivity()
    
    #user input to add cubes
    orangecube={"shape":"cube", "color":"orange"}                 #0
    redcube={"shape":"cube", "color":"red"}                       #1
    cyancube={"shape":"cube", "color":"dark cyan"}                #2
    lbluecube={"shape":"cube", "color":"light blue"}              #3
    purplecube={"shape":"cube", "color":"purple"}                 #4
    cubes_list=[orangecube,redcube,cyancube,lbluecube,purplecube]
    cubes=Cubes(cubes_list)
    tk.bind('<Button-3>',lambda event:e.add_cubes(event,cubes))

    #get dico of cubes
    cubes_dico=cubes.cube_dico

    #user input to add circles
    orangecircle={"shape":"circle", "color":"orange"}                 #0
    redcircle={"shape":"circle", "color":"red"}                       #1
    cyancircle={"shape":"circle", "color":"dark cyan"}                #2
    lbluecircle={"shape":"circle", "color":"light blue"}              #3
    purplecircle={"shape":"circle", "color":"purple"}                 #4
    circles_list=[orangecircle,redcircle,cyancircle,lbluecircle,purplecircle]
    circles=Cubes(circles_list)
    tk.bind('<Button-2>',lambda event:e.add_cubes(event,circles))

    #get dico of circles
    circles_dico=circles.cube_dico

    #user input solve or display one ensemble
    reponse = Entry(tk)
    reponse.grid(row=1, column=1, pady=5, padx=5)
    dsolve=DisplaySolve()
    reponse.bind("<Return>", lambda event:dsolve.solve(event, elements, cubes, circles, c))
    


    tk.mainloop()
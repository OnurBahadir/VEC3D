
import math

class vec3D:

    n=0 #number of created vec3D

    def __init__(self,i=0.0,j=0.0,k=0.0):
        self.i=float(i)
        self.j=float(j)
        self.k=float(k)
        vec3D.n+=1

    def __len__(self):
        return 3-[self.i,self.j,self.k].count(0.0)
   
    def __getitem__(self,v): # ivec[0] 
        if( v==0):
            return self.i
        elif v==1:
            return self.j
        elif v==2:
            return self.k
        else:
            raise NotImplementedError
            
    def __setitem__(self,v,value):   # ivec[0]=1
        if( v==0):
            self.i=value
        elif v==1:
            self.j=value
        elif v==2:
            self.k=value
        else:
            raise NotImplementedError


    @property   #getter
    def x(self):
        return self.i
    
    @x.setter    #setter (properties setter)
    def x(self,val):
        self.i=val
    
    @property
    def y(self):
        return self.j

    @y.setter
    def y(self,val):
       self.j=val
    
    @property
    def z(self):
        return self.k

    @z.setter   
    def z(self,val):
        self.k=val


    def __repr__(self):
        return f"{self.i}i {self.j}j {self.k}k"
    
    @property  # make vec3D.magnitude() to vec3D.magnitude 
    def magnitude(self):
        return (self.i**2+self.j**2+self.k**2)**0.5

    # dot product
    def dot(self,iVec):
        return self.i*iVec.i+self.j*iVec.j+self.k*iVec.k

    def normalized(self):
        mag=self.magnitude()
        self.i=( self.i / mag )
        self.j=( self.j / mag )
        self.k=( self.k / mag )
    
    def normalize(self):
        mag=self.magnitude()
        return vec3D(self.i / mag,self.j / mag,self.k / mag )

    # in degree
    def angleBetween(self,iVec):
        return math.acos((self.i*iVec.i+self.j*iVec.j+self.k*iVec.k)/(self.magnitude()*iVec.magnitude()))*(180.0/math.pi)
    
    #static method functions doesnt access class variables 
    @staticmethod  
    def  ang2rad(ang):
        return ang*math.pi/180

    @staticmethod
    def rad2ang(rad):
        return ang*180/math.pi
    


    #access class variable for every created class
    @classmethod   
    def set_n(cls,value):
        cls.n=value
    
    #use as a constructor
    @classmethod  
    def from_string(cls,string):
        i,j,k=string.split(",")
        return cls(float(i),float(j),float(k))



    #magic-dunder methods https://docs.python.org/3/reference/datamodel.html
    
    # vec1+vec2
    def __add__(self,iVec):
        return vec3D(self.i+iVec.i,self.j+iVec.j,self.k+iVec.k)
    
    # vec1-vec2
    def __sub__(self,iVec):
        return vec3D(self.i-iVec.i,self.j-iVec.j,self.k-iVec.k)

    # vec1 * val
    # vec1 * ved2 cross product
    def __mul__(self,iVec):
        if( isinstance(iVec, float) or isinstance(iVec, int ) ):
            return vec3D(self.i*iVec,self.j*iVec,self.k*iVec)
        
        #else -> cross product
        else:
            return vec3D(self.j*iVec.k-self.k*iVec.j, self.k*iVec.i-self.i*iVec.k,self.i*iVec.j-self.j*iVec.i)


    # vec1 *= val
    # vec1 *= ved2 #cross product
    def __imul__(self,iVec):
        if( isinstance(iVec, float) or isinstance(iVec, int ) ):
            return vec3D(self.i*iVec,self.j*iVec,self.k*iVec)
        else:
            return vec3D(self.j*iVec.k-self.k*iVec.j, self.k*iVec.i-self.i*iVec.k,self.i*iVec.j-self.j*iVec.i)
    
    # vec1 / val
    def __truediv__(self,val):
        if  val!=0:
            return vec3D(self.i/val,self.j/val,self.k/val)
        else:
            raise NotImplementedError()
    
    # vec1 /= val
    def __itruediv__(self,val):
        if  val!=0:
            return vec3D(self.i/val,self.j/val,self.k/val)
        else:
            raise NotImplementedError()

    # vec1 == vec2
    def __eq__(self,iVec):
        return (self.i==iVec.i and self.j==iVec.j and self.k==iVec.k)
    
    # vec1 != vec2
    def __ne__(self,iVec):
        return (self.i!=iVec.i or self.j!=iVec.j or self.k!=iVec.k)

    def __abs__(self):
        return self.magnitude()
    
    # vec1 += vec2
    def __iadd__(self,iVec):
         return vec3D(self.i+iVec.i,self.j+iVec.j,self.k+iVec.k)

    # vec1 -= vec2
    def __isub__(self,iVec):
         return vec3D(self.i-iVec.i,self.j-iVec.j,self.k-iVec.k)
        
    # vec1 < vec2
    def __lt__(self,iVec):
        return self.magnitude()<iVec.magnitude()

    # vec1 <= vec2
    def __le__(self,iVec):
        return self.magnitude()<=iVec.magnitude()

    # vec1 > vec2
    def __gt__(self,iVec):
        return self.magnitude()>iVec.magnitude()

    # vec1 >= vec2
    def __ge__(self,iVec):
        return self.magnitude()>=iVec.magnitude()




    
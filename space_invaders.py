from pyb import UART, Pin, SPI, delay, LED


class Starship_S:
    def __init__(self, x, y, skin):
        self.x = x
        self.y = y
        self.skin = skin

class Monster_S:
    def __init__(self, x, y, skin):
        self.x = x
        self.y = y
        self.skin = skin 

class Bullet_S:
    def __init__(self, x, y, skin):
        self.x = x
        self.y = y
        self.skin = skin

    def erase(self):
        move(self.x,self.y)
        uart.write(" "*len(self.skin))

    def move_up(self):
        self.erase()
        self.y -= 1
        if self.y>0:
            self.y-=1
            move(self.x, self.y)
            uart.write(self.skin)
        else :
            bullet_group.remove(self)
        delay(5)
led1 = LED(1)
led2 = LED(2)
led3 = LED(3)
led4 = LED(4)

uart = UART(2, 115200)

precision = 300
size_width = 300
size_height = 50
x_ord=60

starship = Starship_S(x=size_width//2-5, y=50, skin="V==^==V")
ennemy= Monster_S ( x= x_ord, y= 9, skin="|-v-|" )
ennemy2 = Monster_S (x= 65, y= 15, skin= "[-s-]")
ennemy3= Monster_S (x=x_ord, y= 21, skin= "[-I-]")
bullet_group=[] 

push_button = pyb.Pin("PA0", pyb.Pin.IN, pyb.Pin.PULL_DOWN)
    


CS = Pin("PE3", Pin.OUT_PP)
SPI_1 = SPI(
    1,
    SPI.MASTER,
    baudrate=50000,
    polarity=0,
    phase=0,)


def read_reg(addr):
    CS.low()
    SPI_1.send(addr | 0x80)
    tab_values = SPI_1.recv(1)
    CS.high()
    return tab_values[0]


def write_reg(addr, value):
    CS.low()
    SPI_1.send(addr | 0x00)
    SPI_1.send(value)
    CS.high()


def convert_value(high, low):
    value = (high << 8) | low
    if value & (1 << 15):
        value = value - (1 << 16)
    return value * 2000 / 32768


def read_acceleration(base_addr):
    low = read_reg(base_addr)
    high = read_reg(base_addr + 1)
    return convert_value(high, low)


def clear_screen():
    uart.write("\x1b[2J\x1b[?25l")


def move(x, y):
    uart.write("\x1b[{};{}H".format(y, x))


def add_bullet():
    bullet_group.append(Bullet_S(x=starship.x +3, y=starship.y+1, skin="|"))


def x_pos():
    x_accel = read_acceleration(0x28)
    return x_accel >= precision
  


def x_neg():
    x_accel = read_acceleration(0x28)
    return x_accel <= -precision
        


if __name__ == "__main__":

    addr_who_am_i = 0x0F
    print(read_reg(addr_who_am_i))
    addr_ctrl_reg4 = 0x20
    write_reg(addr_ctrl_reg4, 0x77)

clear_screen()

while ennemy.x < 270:
    move(ennemy.x , ennemy.y) 
    uart.write(" "+ennemy.skin+" ")
    ennemy.x += 10
    

while ennemy2.x < 265:
    move(ennemy2.x , ennemy2.y) 
    uart.write(" "+ennemy2.skin+" ")
    ennemy2.x += 10
    

while ennemy3.x  < 270:
    move(ennemy3.x , ennemy3.y) 
    uart.write(" "+ennemy3.skin+" ")
    ennemy3.x += 10
    


while True:


    if x_pos() == True and starship.x < 290:
        led2.off()
        led3.off()
        led1.on()
        starship.x+=1
        move(starship.x, starship.y)
        
        uart.write(" "+starship.skin+" ")
        delay(30)

    elif x_neg() == True and starship.x > 50:
        led2.on()
        led1.off()
        led3.off()
        starship.x-=1
        move(starship.x, starship.y)
        
        uart.write(" "+starship.skin+" ")
        delay(30)

    while(True):       
        for bullet in bullet_group:
                bullet.move_up()  
    
        if push_button.value() == 1 and len(bullet_group) < 3 :
            add_bullet()
        break
        

   
     
     
     
     
     
     
     
     
     
        
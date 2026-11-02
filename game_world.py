#world = []

world = [[],[]] #0번,1번 레이어를 가지는 2차원 리스트

#게임월드에 객체 추가,layer를 지정해야한다.
def add_object(o,depth = 0): #기본 depth는 0, 즉 0번 레이어에 추가한다.
    world[depth].append(o)

#게임 월드에서 객체 제거(이해하기)
def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return  #더 이상 찾을 필요가 없으므로 return으로 종료.(최적화)

#게임 로직(로직 없애주는 거까지)
def update():
    for layer in world:
        for o in layer[:]:
            o.update()
            #화면 밖에서도 공이 실행되지 않게 함
            if getattr(o, 'is_finished', False):
                remove_object(o)

def render():
    for layer in world:
        for o in layer:
            o.draw()
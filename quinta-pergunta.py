# Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

def lamp_switch_simulation():
    lamps = ["Apagada e fria", "Apagada e quente", "Acesa"]

    # Simulando a lógica descrita:
    switch_to_lamp = {}

    # Primeiro interruptor ligado e desligado
    switch_to_lamp["Interruptor 1"] = lamps[1]

    # Segundo interruptor ligado
    switch_to_lamp["Interruptor 2"] = lamps[2]

    # Terceiro interruptor nunca foi ligado
    switch_to_lamp["Interruptor 3"] = lamps[0]

    return switch_to_lamp

# Exemplo de uso


result = lamp_switch_simulation()
for switch, lamp_status in result.items():
    print(f"{switch} controla a lâmpada que está: {lamp_status}")

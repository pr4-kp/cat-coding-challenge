import random
import matplotlib.pyplot as plt

sample_error_codes = ['111', '001', '101', '011']

def main():
    """ 
    INPUT:

    001 ACK - request connection (beginning of session)
    010 STS - plus a binary number designating fuel system component, to provide status (000 stand for overall status)
    011 LVL - request for fuel level report 
    100 END - request of disconnect (end of session)

    OUTPUT:

    001 ACK - acknowledge
    110 FLT - binary number of Fault Code - alter the failiure of the fuel system or fuel system component
    101 OKY - all is good :) 
    011 LVL - followed by binary number repreentation of current fuel level / fuel level report 
    100 END - acknowledge
    """
    session_in = input().split()
    n = len(session_in)
    i = 0

    fuel_level = 3 # arbitrary 
    fuel_levels = [3]

    # arbitrary, 1 indicates the component is working 
    # 0 indicates the component is not working
    components = [1] * 8 
    
    while (i < n):
        if (session_in[i] == '001'):
            break
        i += 1

    if (i == n):
        return
    
    print(session_in[i], end=' ')
    i += 1

    while (i < n):
        # disconnect 
        if (session_in[i] == '100'):
            print(session_in[i], end=' ')
            plt.plot(fuel_levels)
            plt.title("Fuel Levels")
            plt.xlabel('Time')
            plt.ylabel('Fuel')
            plt.show()
            return
        i += 1

        # status 
        if (session_in[i] == '010'): # requesting for status of a fuel system component
            i += 1
            fuel_level = max(0, fuel_level + random.randint(-1,1))
            fuel_levels.append(fuel_level)

            for k in range(len(components)):
                components[k] = random.randint(0, 1)

            # look through all requests
            for j in range(len(session_in[i]) // 3):
                component_number = session_in[i][3*j:3*(j+1)]

                if (component_number == '000'):
                    # check all components
                    for c in range(len(components)):
                        # check if faulted or okay
                        if (components[c] == 0):
                            print('110 ' + random.sample(sample_error_codes, 1)[0],
                                end=' ')
                        else:
                            print('101', end=' ')  # okay!
                else:
                    # check if faulted or okay
                    if (components[int(component_number, 2)] == 0):
                        print('110 ' + random.sample(sample_error_codes, 1)[0],
                                end=' ')
                    else:
                        print('101', end=' ')  # okay!

        if (session_in[i] == '011'):
            print('011 ' + f'{fuel_level:03b}', end=' ')
    
    
if __name__ == '__main__':
    main()

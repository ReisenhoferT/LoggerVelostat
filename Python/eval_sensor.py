import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

if __name__ == '__main__':

    f_path_data = '/home/cedric/Documents/Code/Arduino/LoggerVelostat/'
    # f_path_user = 'TestCapteur/2inpowervsPowertap/'
    f_path_user = 'Python/'
    f_name = ['data_sans_charge']
    exten = '.csv'

    df = pd.read_csv(f_path_data + f_path_user + f_name[0] + exten)

    # pref = df['2inpower'].tolist()
    temp = df['Temperature'].tolist()
    resistance = df['Resistance'].tolist()
    temp = np.array(temp)
    resistance = np.array(resistance)
    humidite = df['Humidite'].tolist()
    humidite = np.array(humidite)

    # sort data

    sorted_idx = np.argsort(temp)

    temp_sort = temp[sorted_idx]
    resistance_sort = resistance[sorted_idx]

    # ypredict = np.zeros(len(pref_sort))
    # slope, intercept, r_value, p_value, std_err = stats.linregress(pref_sort,
    #                                                                po_sort)

    # if b_proc_energy is True:
    #     pref_moy, po_moy = process_energy(pref_s, po_s, crop)
    #     pref_moy = np.array(pref_moy)
    #     po_moy = np.array(po_moy)
    #     s_e, inter_e, r_val_e, p_val_e, _ = stats.linregress(pref_moy,
    #                                                          po_moy)

    # for i in range(len(po_sort)):
    #     ypredict[i] = intercept + pref_sort[i] * slope

    # std_model = np.std(po_sort - ypredict)

    # if b_proc_energy is True:
    #     y_p_e = np.zeros(len(po_moy))
    #     for i in range(len(po_moy)):
    #         y_p_e[i] = inter_e + pref_moy[i] * s_e

    #     std_model_e = np.std(po_moy - y_p_e)

    # print("Results for all power values : ")
    # print("R2 : ", r_value**2)
    # print("p value : ", p_value)
    # print("Slope : ", slope)
    # print("Intercept : ", intercept)
    # print("MSE : ", std_model)

    plt.figure(1)
    plt.plot(temp_sort, resistance_sort, 'o', label='raw data')
    plt.xlabel('Temperature')
    plt.ylabel('Resistance')
    # plt.plot(pref_sort, ypredict, 'r', label='model')
    # plt.plot(pref_sort, (intercept + 2 * std_model) + pref_sort * slope, '--y',
    #          label='+2 sigma')
    # plt.plot(pref_sort, (intercept - 2 * std_model) + pref_sort * slope, '--b',
    #          label='-2 sigma')
    plt.legend()

    sorted_idx = np.argsort(humidite)

    humidite_sort = humidite[sorted_idx]
    resistance_sort = resistance[sorted_idx]

    plt.figure(2)
    plt.plot(humidite_sort, resistance_sort, 'o', label='raw data')
    plt.xlabel('Humidite')
    plt.ylabel('Resistance')
    plt.legend()

    plt.show()

def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc, f_perc, nb_perc for your results
    ##################################################
    """
    
    m_num = int(input("Number of males: "))
    f_num = int(input("Nuumber of females: "))
    nb_num = int(input("Number of non-binary people: "))

    total = m_num + f_num + nb_num
    m_perc = m_num * 100 / total
    f_perc = f_num * 100 / total
    nb_perc = nb_num * 100 / total

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    print(
        f'The percentage of males, females and non-binary \t {m_perc: .2f} \t {f_perc: .2f} \t {nb_perc: .2f}')
    return m_perc, f_perc, nb_perc


if __name__ == '__main__':
    main()

def version_compare( version1, version2 ) :
	 #Insert your code here
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))

    max_length = max(len(v1), len(v2))
    v1.extend([0] * (max_length - len(v1)))
    v2.extend([0] * (max_length - len(v2)))

    if v1 == v2:
        return -1
    elif v1 < v2:
        return 0
    elif v1 > v2:
        return 1


def version_compare( version1, version2 ) :
	 #Insert your code here
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))


    max_length = max(len(v1), len(v2))
    v1.extend([0] * (max_length - len(v1)))
    v2.extend([0] * (max_length - len(v2))) 

    print(v1, v2)
    if v1 < v2:
        return -1
    elif v1 == v2:
        return 0
    elif v1 > v2:
        return 1



print('RESULT', version_compare( '2','2.0.0.0.0'))
print('RESULT', version_compare( '2','2.1.0.0.0'))
print('RESULT', version_compare( '3','2.0.0.0.0'))

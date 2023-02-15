class A:
    publicV = "Public"
    _protectedV = "Protected"
    __privateV = "Private"
    def PublicFunc(pb):
        print(pb)

AA = A
AA.PublicFunc(AA.publicV)
AA.__privateV = 1
AA.PublicFunc(AA._protectedV)
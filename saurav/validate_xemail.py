
class validateEmail:
    def validate(email):
        x=email.split("@")
        if len(x)==2:
            domain=['gmail.com',"outlook.com","example.com","example.net"]
            if x[-1] in domain:
                if len(x[0]) != 0:
                    return True
                else:
                    return False
            else:
                return False
            
        else:
            return False
        

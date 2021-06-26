class Driver extends Account
{
    constructor(account, email, password)
    {
        super(account);
        
        this.account = account;
        this.email = email;
        this.password = password;
    }
}
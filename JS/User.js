class User extends Account
{
    constructor(account, email, password)
    {
        super(account, email, password);

        this.account = account;
        this.email = email;
        this.password = password;
    }
}
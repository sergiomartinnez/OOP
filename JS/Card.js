class Card extends Payment{
    constructor(id, cardName, CardNumber, cvv, expirationDate){
        super(id);
        this.cardName = cardName;
        this.CardNumber = CardNumber;
        this.cvv = cvv;
        this.expirationDate = expirationDate;
    }
}
class Card extends Payment {
    Integer id;
    String cardName;
    Integer cardNumber;
    Integer cvv;
    Integer expirationDate;

    public Card(Integer id, String cardName, Integer cardNumber, Integer cvv, Integer expirationDate){
        super(id);
        this.cardName = cardName;
        this.cardNumber = cardNumber;
        this.cvv = cvv;
        this.expirationDate = expirationDate;
    }
}

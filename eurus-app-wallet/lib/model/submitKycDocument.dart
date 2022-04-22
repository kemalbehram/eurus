class SubmitKycDocument {
  int returnCode;
  String message;
  String nonce;
  Null data;

  SubmitKycDocument(this.returnCode, this.message, this.nonce, this.data);

  SubmitKycDocument.fromJson(Map<String, dynamic> json)
      : returnCode = json['returnCode'],
        message = json['message'],
        nonce = json['nonce'],
        data = json['data'];

  Map<String, dynamic> toJson() => {
        'returnCode': this.returnCode,
        'message': this.message,
        'nonce': this.nonce,
        'data': this.data,
      };
}

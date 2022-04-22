export enum ServerReturnCode {
	Success = 0,
	UnauthorizedAccess = -1,
	MethodNotFound = -2,
	InvalidSignature = -3,
	RequestMalformat = -4,
	InternalServerError = -5,
	InvalidSession = -6,
	LoginTokenExired = -7,
	LoginTokenInvalid = -8,
	DatabaseError = -9,
	SignMatchError = -10,
	RefreshTokenError = -11,
	RevokeTokenError = -12,
	NetworkError = -13,
	RequestParamsValidationError = -14,
	EthereumError = -15,
	TimestampError = -16,
	ServerIdUnmatch = -17,
	RequestTooFrequenct = -18,
	BadRequest = -20,
	UserNotFound = -21,
	InvalidArgument = -22,
	RecordNotFound = -23,
	UserStatusForbidden = -24,
	ServerTokenInvalid = -25,
	UniqueViolationError = -26,
	HttpStatusCodeBegin = -1000,
	HttpStatusCodeEnd = -1999,
}

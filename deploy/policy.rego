package admin

default allow  = false

allow {
  input.user.is_superuser
}
NAME    := protobuf-c
SRC_EXT := gz
SOURCE   = https://github.com/protobuf-c/protobuf-c/releases/download/v$(VERSION)/$(NAME)-$(VERSION).tar.$(SRC_EXT)

include packaging/Makefile_packaging.mk
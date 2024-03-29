Summary:	DevHelp book: glib 1.2
Summary(pl.UTF-8):	Książka do DevHelpa o glibie 1.2
Name:		devhelp-book-glib
Version:	1.2
Release:	1
License:	GPL
Group:		X11/Applications
#Source0:	http://www.devhelp.net/books/books/glib-1.2.tar.gz
Source0:	glib-1.2.tar.gz
# Source0-md5:	926ae606284b1e2aba25b965ea54045e
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about glib 1.2.

%description -l pl.UTF-8
Książka do DevHelpa o glibie 1.2.

%prep
%setup -q -c -n glib-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/glib-%{version},specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/glib-%{version}.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/glib-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*

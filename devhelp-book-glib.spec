Summary:	DevHelp book: glib
Summary(pl):	Ksi±¿ka do DevHelp'a o glib
Name:		devhelp-book-glib
Version:	1.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/glib-1.2.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about glib 1.2

%description -l pl
Ksi±¿ka do DevHelp o glib 1.2

%prep
%setup -q -c glib-%{version} -n glib-%{version}

%build
mv -f book glib-%{version}
mv -f book.devhelp glib-%{version}.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/glib-%{version}
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install glib-%{version}.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install glib-%{version}/* $RPM_BUILD_ROOT%{_prefix}/books/glib-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs

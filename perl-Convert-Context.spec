%define		pdir	Convert
%define		pnam	Context
Summary:	Convert::Context Perl module - an attributed text data type
Summary(pl.UTF-8):	Moduł Perla Convert::Context - typ danych: tekst z atrybutami
Name:		perl-Convert-Context
Version:	0.501
Release:	13
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	701f73725e44b34f89a0cba23e74d672
URL:		http://search.cpan.org/dist/Convert-Context/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::Context module maintains attributed strings. It allows you to
access those strings similiar to Perl's normal strings.

%description -l pl.UTF-8
Moduł Convert::Context zarządza łańcuchami tekstowymi z
przyporządkowanymi atrybutami. Umożliwia dostęp do tych łańcuchów w
podobny sposób jak do normalnych łańcuchów Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_archlib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Convert/Context.pm
%{_mandir}/man3/*

%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	Context
Summary:	Perl Convert::Context module
Summary(pl):	Modu³ Perla Convert::Context
Name:		perl-Convert-Context
Version:	0.501
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	701f73725e44b34f89a0cba23e74d672
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::Context allows you to access attributed strings similiar to
perl's normal strings.

%description -l pl
Convert::Context umo¿liwia dostêp do ³añcuchów z przyporz±dkowanymi
atrybutami w podobny sposób jak do normalnych ³añcuchów.

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

%include	/usr/lib/rpm/macros.perl
Summary:	Perl Convert-Context module
Summary(pl):	Modu³ Perla Convert-Context
Name:		perl-Convert-Context
Version:	0.501
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Convert/Convert-Context-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert-Context allows you to access attributed strings similiar to
perl's normal strings.

%description -l pl
Convert-Context umo¿liwia dostêp do ³añcuchów z przyporz±dkowanymi
atrybutami w podobny sposób jak do normalnych ³añcuchów.

%prep
%setup -q -n Convert-Context-%{version}

%build
perl Makefile.PL

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_archlib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Convert/Context.pm
%{_mandir}/man3/*
